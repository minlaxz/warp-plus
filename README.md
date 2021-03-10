more and more data for warp-plus
===

Description : ~~limited warp plus Cloudflare account~~

1. Clone this repo
2. Build docker image
3. Run docker container
    
    ```docker run -d -p 8000:5000 -v $PWD:/app --restart unless-stopped --memory='512m' --cpus=0.5 IMAGE:VERSION```

4. Expose private port to public here are [examples](https://github.com/anderspitman/awesome-tunneling)

    For me : ssh -v -R 80:localhost:8000 localhost.run

5. visit localhost.run generated link.

**OR you can also pull prebuilt docker image**

from docker hub > 
```docker pull minlaxz/warp-plus:latest```

or alternatively from github packages >
```docker pull docker.pkg.github.com/minlaxz/warp-plus/warp:1.0```

then follow steps _3_, _4_ and _5_