# MultiStreamGUI

A simple GUI for Streaming on multiple platforms with OBS using a NGINX RTMP server.

## Dependencies

You need to have Stunnel installed and configured. (for Facebook live streaming)

### Configure Stunnel

1. [Download Stunnel](https://www.stunnel.org/downloads.html)
2. Install Stunnel and run it with **stunnel GUI start**
3. Once the GUI is open click on Configuration -> Edit Configuration
4. Ad the following lines at the end of the file and then close it

    ```conf
        [fb-live]
        client = yes
        accept = 127.0.0.1:19350
        connect = live-api-s.facebook.com:443
        verifyChain = no
    ```

5. Reload Stunnel Configuration from Configuration -> Reload Configuration and you are done.

## How to use

1. [Download and extract the latest release](https://github.com/mihaif7/MultiStreamGUI/releases)
2. Run MultiStreamGUI.exe
3. Enter your RTMP Keys from Youtube/Facebook
4. Start Stunnnel and NGINX
5. Configure OBS to stream to Custom Server **rtmp://127.0.0.1/live** and any Stream Key
6. Click start streaming and enjoy :)

<br>
If there is anything I can improve, please let me know.
