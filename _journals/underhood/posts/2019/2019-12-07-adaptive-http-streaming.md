---
layout: post
title:  "Adaptive HTTP Streaming Technologies: The Problem Statement"
date:   2019-12-06 21:12:01 +0100
categories: media
icon: assets/icons/streaming.png
author: by Željko Obrenović
permalink: adaptive-http-streaming
excerpt: "Adaptive HTTP Streaming technologies enable distributing video efficiently via the standard HTTP infrastructure and CDNs. These technologies offer three key elements that the technologies introduce to solve critical challenges: segmentation of video content in smaller blocks to minimize overhead, improve user experience, and improve caching performance, adaptivity by having multiple channels of variable quality to enable automatic switching among channels based on the device characteristics and network performance, and securing the video content while keeping the benefits of efficient HTTP content distribution."

---

> **KEY POINTS:**
>
> * Adaptive HTTP Streaming technologies enable distributing video efficiently via the standard HTTP infrastructure and CDNs.
> * These technologies offer three key benefits: segmentation of video files, adaptive switching among resolutions, and efficient implementation of necessary security measures.

## Intro

As a CTO of my previous company ([incision.care](https://incision.care)), we were building a custom online video-on-demand platform. Consequently, I needed to dig deeper into one technology: Adaptive HTTP Streaming. Examples of this technology are **MPEG-DASH**, **Apple HLS**, **Microsoft Smooth Streaming**, and **Adobe HDS**. While they are subtle differences among these technologies, they share the same general idea: distributing video efficiently via the standard HTTP infrastructure.

A fair amount of material exists on these technologies, covering many technical details (see references at the end of this article). However, when I was explaining and educating people about these technologies, I could not find a good explanation of the basics, general principles, and motivation. In other words, while it is clear that Adaptive HTTP Streaming technologies are widely used and provide the right solution, it is not always clear what the problem is that these technologies are solving. With this post, I want to share my understanding of the adaptive HTTP streaming technologies and their problems, complementing existing comprehensive sources with a more general overview.

I will start by explaining the situation of video delivery without adaptive HTTP streaming technologies and then add elements that the technologies introduce to solve critical challenges:

* **segmentation** of video content in smaller blocks to minimize overhead, improve user experience, and improve caching performance
* **adaptivity** by having multiple channels of variable quality, to enable automatic switching among channels based on the device characteristics and network performance, and
* **securing** the video content while keeping the benefits of efficient HTTP content distribution


## Situation Without Adaptive Streaming

To distribute videos via HTTP, technologies such as Adaptive HTTP Streaming are not necessary. You can put your video file (e.g., an MP4 recording) as a static file on an HTTP server, and reference it from a player in your browser (Figure 1).

![](/assets/images/adaptive-http-streaming/big_video_file.png)
**Figure 1**: *Videos can be distributed via HTTP as a big file.*

This approach is simple, and works reasonably well if your video file is small, you have a good Internet connection, and you do not need to protect the video. This approach has several drawbacks, that Adaptive HTTP Streaming technologies aim at solving:

* The unit of data transfer is a big file, which nowadays can easily be few GBs even for relatively short videos. Transferring such a file generates **significant network traffic**. If you access a file through the mobile network, **latency** can be a huge problem, resulting in an inferior user experience.
* Big files are **less likely to get cached** on devices and proxies.
* When you **jump to some time** in the video, you will need to wait until the browser downloads the content from the beginning of the file to the selected time. In addition to poor user experience, this action generates **unnecessary traffic** as you are downloading more video content, then you are playing.
* With a single big video file, you serve **the same quality** of video to all devices, even though some of them have a lower resolution (devices will also waste processing power to transform the video to a lower resolution).
* If there is **an error in network transfer**, a whole file may need to be downloaded again, introducing additional network traffic and delays.
* User experience can be poor as **the network quality decreases**, directly leads to increased latency.

## Improvement #1: Segmentation

The first improvement that Adaptive HTTP Streaming technologies introduce is segmentation. Instead of serving one big video file, with Adaptive HTTP Streaming technologies, we are splitting that file into multiple small segments. Each segment is stored in a small file (typically few megabytes big and few seconds long). The playlist is also needed to provide basic metadata and a list of URLs for all the segment files (Figure 2). The video player needs a reference the playlist. When the playback starts, the player will begin to download segments from the list and play them. Segmentation is the reason why the discussed video technology are called "streaming" technologies as we are not downloading the whole video but are continouly receveing a stream of video segments.

![](/assets/images/adaptive-http-streaming/step_1_fragmentation.png)
**Figure 2**: *Adaptive HTTP streaming technologies split a big video file in many smaller segments that can be distributed independently.*

Segmentation is a more complex approach than serving a single video file as now videos need to be transcoded to generate segment files and playlists. After segmentation has been done, however, the segment files and playlists can be distributed as static files via conventional HTTP infrastructure and CDNs.

The segmentation offers several advantages over serving a single big video file:
* The unit of data transfer is **a small file**. Such files can be transferred in parallel, and are more likely to be cached (in a browser, proxies, and CDNs).
* This approach generates **much less unnecessary traffic** as you are downloading only the content then you are playing. When you jump to some time in the video, you do not need to download all video content before the selected moment. The video player will continue to download the video segment starting few seconds from the specified time without the need to download all previous segments.
* If there is **an error in network transfer**, only a small file may need to be downloaded again, reducing network transfer and delays.

While the segmentation is an improvement, it alone does not solve the last problem we described with serving a single big video file (Figure 3):
* You are still serving **the same quality** of video to all devices, even though some of them have lower resolution.
* If the network quality drops, **delays** may occur immediately.

![](/assets/images/adaptive-http-streaming/step_1_network_performance.png)
**Figure 3**: *Splitting the video into segments do not solve the problem of buffering.*


## Improvement #2: Multiple Streams

The second improvement that Adaptive HTTP Streaming technologies offer is the introduction of multiple fragmentations of different quality and size. Instead of creating only one playlist of segments with one resolution, you can create multiple lists of segments, each with different resolutions (normally at least three resolutions are used, low, medium, and high). Lower resolution files are smaller and faster to download than higher resolution files. Now your video is being distributed as a collection of segments with different resolutions, a playlist for each resolution, as well as a single index playlist, referencing all other playlists (Figure 4). The video player needs a link to the index playlist, and will then play one or the other playlist depending on the device characteristics and network situation.

![](/assets/images/adaptive-http-streaming/step_2_multiple_streams.png)
**Figure 4**: *Adaptive HTTP streaming technologies split a big video file in smaller fragments that can be distributed independently.*

Having multiple streams for the same video enables **adaptive behavior**. First, if a device cannot play high resolution, the video playback can immediately choose to work with lower resolutions, reducing the network traffic, and reducing the rendering processing at the device. If a device can play high resolutions, the player may start the playback of the high-resolution stream. However, if during the playback the network quality drops, the video player will notice that it may take more time to download video segments than to play them. To avoid pausing playback, the player can play smaller fragments from a lower resolution stream. Only when the lowest resolution segments cannot be downloaded on time, the video will be paused, and the user will need to wait (Figure 5).


![](/assets/images/adaptive-http-streaming/step_2_network_performance.png)
**Figure 5**: *Splitting the video into segments do not solve the problem on unnecessary traffic and delays.*


## Improvement #3: Efficient Security Implementation

Lastly, the Adaptive HTTP Streaming technologies also enable efficient implementation of security measures, without losing the benefits of video distribution via content delivery networks (CDNs).

The protection is achieved by serving **encrypted** segments via a CDN, but requiring authentication of a user to get the key that the player will use to decrypt downloaded segments (Figure 6).

![](/assets/images/adaptive-http-streaming/step_3_protection.png)
**Figure 6**: *Securing the video segments distributed via CDNs.*

This approach keeps all the benefits of segmentation and adaptivity to optimize the data transfer while still protecting the content.

The price is complexity, as we need to build a transcoding process that encrypts the video, we need a safe key management system, and we need to build APIs that protect access to the key.


## Appendix

### To Probe Further

> 1. [**MPEG-DASH vs. Apple HLS vs. Microsoft Smooth Streaming vs. Adobe HDS**](https://bitmovin.com/mpeg-dash-vs-apple-hls-vs-microsoft-smooth-streaming-vs-adobe-hds/), Christopher Mueller, 2015
> 1. [**HTTP Live Streaming**](https://en.wikipedia.org/wiki/HTTP_Live_Streaming), Wikipedia
> 1. [**Dynamic Adaptive Streaming over HTTP**](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP), Wikipedia
> 1. [Adaptive Streaming]()https://bitmovin.com/adaptive-streaming/)



### Key Terminology

>
> * **HLS**: HTTP Live Streaming
> * **DASH**: Dynamic Adaptive Streaming over HTTP
> * **MPEG**: Moving Picture Experts Group
> * **Encoding**: the process of converting data into a format required for a number of information processing needs
> * **Decoding**: the process of converting code into plain text or any format that is useful for subsequent processes (reverse encoding)
> * **Transcoding**: the conversion of one encoding to another, such as for movie data files, audio files (e.g., MP3, WAV), or character encoding (e.g., UTF-8, ISO/IEC 8859)
