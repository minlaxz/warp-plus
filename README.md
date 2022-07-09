Unlimited data for Cloudflare warp-plus
===

Inspired by [Original Author](@ALIILAPRO) :+1:

Description : Cloudflare's ~~warp account~~, no this is warp plus!

1. Clone this repo
2. Build docker image
3. Run docker container

    ```docker run -d -p 8000:5000 -v $PWD:/app --restart unless-stopped --memory='512m' --cpus=0.5 IMAGE:VERSION```
4. That's it!

5. To expose your private port (local) to public internet here are some awesome [examples](https://github.com/anderspitman/awesome-tunneling)

    I chose : ssh -v -R 80:localhost:8000 localhost.run

6. `localhost.run` will generate a _link_ and *visit it.


**OR you can also pull pre-built docker image**
--

from docker hub > 
```docker pull minlaxz/warp-plus:1.1```

from github container registry >
```docker pull ghcr.io/minlaxz/warp-plus/warp:1.1```

then re-follow the steps _3_, (_4_), _5_ and _6_

The other thing needed to be mentioned is that, I simply made this work using [deta.sh](https://deta.sh).

You can hopefully get **warp plus data** using this [link](https://mvtvso.deta.dev/), of course, it is free of charge 😏.