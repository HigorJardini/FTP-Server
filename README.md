## Simple FTP Server in Python3
  <div align="center">
    <img src="https://i.imgur.com/ic5re50.png" width="60px">
  </div>
  
  <p align="center" width="100%">
       <img src="https://i.imgur.com/TskTw6r.png">
  </p>

  <div align="center">
    <img src="https://i.imgur.com/ic5re50.png" width="60px">
  </div>

  - Requirements
    - Python3
    - Pip3
    - Twisted
    - Optional
      - Filezilla

  - How to install Twisted on Ubuntu
    - Use to case your terminal is ZSH
      - ```
          exec bash -- or add PATH on .zsh
        ```
    - ```
      sudo apt install python3-twisted
      ```

  - How to start a ftp server with **Twisted**.
    ```
    twistd3 -n ftp
    
    ## Check on terminal is opened FTP server and FTPFactory createad a port

    2023-01-22T13:09:21-0300 [twisted.scripts._twistd_unix.UnixAppLogger#info] twistd 18.9.0 (/usr/bin/python3 3.8.10) starting up.
    2023-01-22T13:09:21-0300 [twisted.scripts._twistd_unix.UnixAppLogger#info] reactor class: twisted.internet.epollreactor.EPollReactor.
    2023-01-22T13:09:21-0300 [-] FTPFactory starting on 2121 ## Port
    2023-01-22T13:09:21-0300 [twisted.protocols.ftp.FTPFactory#info] Starting factory <twisted.protocols.ftp.FTPFactory object at 0x7f55daed2e20>
    
    ## FTP Server is closed
    2023-01-22T13:09:45-0300 [-] Received SIGINT, shutting down.
    2023-01-22T13:09:45-0300 [-] (TCP Port 2121 Closed)
    2023-01-22T13:09:45-0300 [twisted.protocols.ftp.FTPFactory#info] Stopping factory <twisted.protocols.ftp.FTPFactory object at 0x7f55daed2e20>
    2023-01-22T13:09:45-0300 [-] Main loop terminated.
    2023-01-22T13:09:45-0300 [twisted.scripts._twistd_unix.UnixAppLogger#info] Server Shut Down.
    ```
   - Twisted ftp help:
     - ```
        higor@higor-note:~$ twistd3 -n ftp --help
        Usage: twistd [options] ftp [options].
            WARNING: This FTP server is probably INSECURE do not use it.
        Options:
              --auth=            Specify an authentication method for the server.
              --help             Display this help and exit.
              --help-auth        Show all authentication methods available.
              --help-auth-type=  Show help for a particular authentication type.
          -p, --port=            set the port number [default: 2121]
              --password-file=   Specify a file containing username:password login info
                                 for         authenticated connections. (DEPRECATED; see
                                 --help-auth instead)
          -r, --root=            define the root of the ftp-site. [default:
                                 /usr/local/ftp]
              --userAnonymous=   Name of the anonymous user. [default: anonymous]
              --version          Display Twisted version and exit.
        ```

