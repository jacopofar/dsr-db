---
# You can also start simply with 'default'
theme: default
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
# background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: "Docker: an overview"
info: |
  made for Data Science Retreat
  by Jacopo Farina

  Using [Sli.dev](https://sli.dev)
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
---

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  background-clip: text;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}

.slidev-layout h1 + p {
  opacity: 0.9;
}
</style>

# Docker: an overview

Data Science Retreat

Jacopo Farina

<!-- <div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div> -->

<!-- <div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div> -->

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---

# The problem of the state

Imagine you are developing an app/model/tool...

You try a library or a different version of Python, and:

* You cannot easily reconstruct what exactly is installed now and communicate it
* Different versions of the same thing are installed, and sometimes one or the
  other is used
* A newer version of a software X has been released, if you
  install X on a new machine, it’s not the same you used in
  development, and may break

<!-- <br>
<br>

Read more about [Why Slidev?](https://sli.dev/guide/why) -->

<!--
You can have `style` tag in markdown to override the style for the current page.
Learn more: https://sli.dev/features/slide-scope-style
-->



<!--
Here is another comment.
-->

---

# The problem of the state

You developed a software, (e.g. a web application) depending on a few libraries
and maybe requiring databases and frameworks installed on the system.

* Can you install it on a new machine and be reasonably sure it will work
  the same way?
* Can you make it easy for someone else to run it?
  (Or for yourself in the future)
* Did you update something? Now the change has to be replicated on each
  installation on the same way
* Are there manual changes (e.g. a config file was changed, some command
  copy-pasted and now forgotten)? Now the app behaves in different ways on
  different machines 😱😱
---

# What about security?

Everything you run can read/write your files, access the network, see other
processes.

This is a problem not only for *deliberate* attacks, but also trivial mistakes.

> Oops, my script runs `rm -rf /home/john /dataset.parquet`
>
> and now my home folder is gone ☠️

Isolating applications is useful in general

For example, I have multiple independent projects requiring a Postgres instance.
If I had a single instance on my computer everything would be mixed up, I prefer
to have a specific version of Postgres with a data folder whose size I can
monitor.

---

# What is Docker

* Runs a Linux process in an isolated and controlled way, in a so-called
  *container* (sometimes called *jail*)
* Can be used during development and/or production
* Prevents apps access to the "real" filesystem, network and processes
* Allows reproducible build and execution (no *works on my
machine* ™)
* Available for macOS and Windows using a virtual machine
* There is also a native Docker for Windows, but is not that common

---

# Other approaches

The problem is very common, many came with solutions to it:

* ***Conda*** isolates a Python environment. Almost only for Python, and may not
  cover all libraries.
* ***Nix*** is similar in scope, but focuses on reproducibility alone rather
  than isolation
* ***virtualenv*** similar to Conda, included in Python, no curated list of
  libraries

...and many more.

Docker is one of the **most common** solutions and tries to be **universal**.

Additionally, *containers* are the foundation of tools like Kubernetes or
 Compose, extremely common in enterprise environments.

---

# Server and client

The daemon (dockerd) is the process that manages all docker resources
* Also known as engine
* On macOS and Windows, it runs in a Linux VM

The Docker client (docker) is the primary way that Docker users interact with
the Daemon
* Can run directly on non-Linux system
* Communicate with the engine via HTTP

In our case, the daemon and the client will be on the same machine: our
laptops!

---

# Images and containers

An image is a template to create containers to run. Most importantly, it
contains all the files visible to the running app (including libraries and
intepreters).

Roughly, you can see the image as a copy of the disk of a computer with some
app installed and ready to use.

There are repositories of useful public images, for example at hub.docker.com
and **private** repositories for companies.

A container is a running image, you can have multiple containers from the
same image.

Every container is based on one and only one image, but an image can be
executed in many different containers

> Can be useful to see an image like an app you can double-click multiple times,
 getting multiple windows (containers), independent from each other and with
 their own state.

> The image defines the initial state of a container and does
 not change across excutions.

---

# Recap:

![schema showing the main components of Docker, images containers and repositories](./docker_images_containers_recap.png)

---

# Enough talk, let's see this in action!

Let’s say we want to check how this code behaves in different Python versions:

```python
print(f'this is {3+2}')
```
installing Python 3.5 and 3.12 on the same machine is boring and can be messy.

It's a good use case for Docker: we want to isolate the environment.

> Another way to see it is to think about phone apps:
 you can install an app and it will not affect other apps, when removed is gone

---

# Step 1: find the image details

Since this is Python, a very common language, we safely assume there's an image
somewhere in the public registry.

Go to [hub.docker.com](https://hub.docker.com/) and search for python.


Image names are represented this way:


 ```{docker hub username}/{image}:{tag}```

If the tag is omitted, it is `latest` by default

When an image is official, you can omit the username.

In this case `python:3.5` is what we need (username is omitted because it
 is an official image)


---

# Step 2: download the image

Use:

* `docker pull` to download an image
* `docker images` to list the downloaded images
* `docker rmi` to delete an image

Notice that images are versioned and have an hash.

Docker commands accept both the image name or the hash.

---

# Step 3: run a container from the image

Use:

* `docker run` to start a container from an image

  Some essential flags:
  * `-it` to run it in interactive mode
  * `--rm` to delete upon exit
  * `--name` to give it a name (if not, it uses a random one)
* `docker ps` to see the running containers
* `docker stop / kill / rm` to stop and delete the containers
* `docker inspect` to see all the details (lots of details, useful for troubleshooting)
* `docker system prune` can delete all stopped containers to save space

---

# Let's play with the filesystem

Create a container with:
`docker run -it --rm --name mypython python:3.9`
* Use `docker ps` in another window to see the running container
* Use `docker exec -it mypython bash` to start bash in this container,
 and write to a file
* You can also use `docker run -it --rm --name mypython python:3.9 bash` to start
bash instead of python in a container
* Can you read the file from python?
* What happens if you start another container, is the file there?

Hint: If you miss the `--rm` flag you can use `docker ps -a` to see stopped
containers, `docker rm` to eliminate them

---

# Each container has its own filesystem

From "inside" a container, you see the filesystem *initialized* from the image.

A container can modify files, but changes are only for that container and
are ephemeral.

This is **by design**, to make every process **reproducible**.

If you need to configure/install components not provided by the image, you
need to create your own image (we are going to see this).

What about datasets and models?
You can mount **volumes** to process data from the outside

---

# Mount volumes and folders

Sometimes you actually want to read/write files from a container and make them
persistent.

Use the `-v` flag to **mount** volumes or folders when you start a container.

add `-v myvolume:/my_mount_point` to add a volume called "`myvolume`" and make it
visible under `/my_mount_point`.

Use a path (absolute, starting with `/`) instead of a volume name to mount a
folder from your computer.

Tips:

* You can add `:ro` to make the mount read-only (`-v myvolume:/mountpoint:ro`)
* Files created from containers on mounted folders can have weird permissions
metadata, if needed use `chown` and `chmod` to fix them
* You can use `-v` multiple times to mount multiple volumes
* Trick: you can use `docker cp` to copy files in and out from containers, if
 you forgot to mount a volume
* Trick 2: you can use `docker diff` to see which files where touched by a
 container

---

# See the output

The `-it` flag starts an intractive container, while `-d` starts one in
 background.

You can try it easily with
 `docker run -d --rm --name pinger python:3.5 ping google.com`.

Now you can use `docker logs -f pinger` to follow the logs (Ctrl + C to quit).

Additionally, `docker attach pinger` tries to "reconnect" to an existing
 container.

Server applications like databases or Ollama usually are executed in background
 and expect connections from clients rather than being used from the shell.

---

# Environment variables

A container does not see the system environment variables

It receives the environment variables defined in the image, additional
environment variables can be passed using the -e flag when running a container.

This is a common way to pass the configuration (API keys, password, etc.),
 another one is to mount volumes with the secrets as files.

`docker run -it --rm -e BLA=5 python:3.5 bash`

now `echo $BLA` inside the container will show the value, every process in the
 container can read it.

---

# Intermission: networking

Before seeing how Docker handles networking, let's see the basic concepts of
 how to represent connections and services *in practice*. This is **essential**
 knowledge even outside Docker. We'll skip many details for simplicity.

---

# Intermission: networking

### IP addresses and hostnames

Each node in a network (really each `interface`) receives an IP address
identifying it, e.g. `192.168.1.7`. For convenience, there are tools
(like the `DNS`) to map IPs to names like `google.com` or `localhost`.

Use `ping someaddress` to see the IP associated ("resolved") to an hostname.

In a common setup (at DSR or in a company or at home) you have three IPs you
 care about:

* `127.0.0.1`, also called `localhost`. A special address referring to yourself,
 in a Docker container is the container itself rather than the whole machine

* A private/local address, like `192.168.1.7`, valid only within the same network.
 You can see it with the command `ip addr show` or `ifconfig`, `ipconfig` on
 Windows. Some networks are configured to not allow communication between nodes.
 It's the address you use for example for a local printer.

* An internet/public address, assigned to the router. Usually same for all the
 computers in the network, you can see if for example at
 [whatismyip.com](https://www.whatismyip.com/)

---

# Intermission: networking

When you run an application, e.g. a web app, you can then connect in different
 ways:

* Using `localhost` / `127.0.0.1` to test it on the same machine (or container)
* Using the private address to share it across the same network, if allowed
* If deployed on a server with a dedicated public address, that address. May have
 to be purchased, depends on the hosting service

A few tips:

* You can rent a domain name to map to your IP address
* For testing, tools like `ngrok` or `bore` expose temporarily something local
 to a public address
* Many servers need to be **told** to listen on all available IPs. `0.0.0.0` is
 a "special" IP to indicate that every available interface is being used.
* These details are for IPv4, IPv6 are still uncommon but the same principles
 remain valid

---

# Intermission: networking

### Ports

IPs identifies a computer (well, an interface really), but a computer can run
 different services at the same time. To tell them apart, you have also a `port
 number` between 1 and 65536.

When you visit an address like `http://localhost:3000` you are connecting not
 just to `localhost` but to the specific service using port 3000. When you use
 a web server tool like Streamlit or Flask or Fastapi you have to specify a
 port or get a default one.

A few notes:

 * Some port numbers are standard and may be omitted. For example `http` implies
 port 80, `https` is port 443, so `http://john.com` is using port `80` by
 default
 * You may have already something using some ports, e.g. AirPlay may use 8000
 * Starting a server ("listening") on ports below 1024 requires root permissions
 and is usually a bad idea because they are likely associated with
 standard services.
 * Commands like `lsof` or `netstat` can show who's using which port, also the
 GUI usually shows it

---

# Networking in Docker

Docker isolates the network as well!

* Each container by default has an IP address (visible with `docker inspect`)
 which makes sense only locally
* Use `-p 8090:3000` to expose port `3000` of the container to the port `8090`
 of your computer. The container "believes" it's using 3000, but
 `localhost:8090` will show it.
* On Docker Desktop / rancher desktop you also have the VM in the middle, so
 may need extra config depending on the case.

---

# Let's try it

Did you know Python comes with an incorporated web server?

Yep, try `python3 -m http.server`. You can specify a port with
 `python3 -m http.server 4567`.

This is very useful when doing frontend development or to share files.

Try it locally and in Docker, you should be able to use `-p` to make it visible
 on the

Note: there are many tools like this from Python, see https://docs.python.org/3/library/cmdline.html

---
dragPos:
  square: 56,1888,0,0
---

# A more complete example: Postgres

Go to the Docker Hub and follow the instructions to start a Postgres server.

Should be something like:

`docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

now you can connect from within the container using `docker exec`.

The command to open a postgres shell is
`psql postgresql://postgres@ipaddress:port`, the port by default is `5432` and
can be omitted if that's the case.

This is a *real* postgres instance, you can use it from DB clients or Python
libraries. You have to mount a volume to persist the data, though.

---

# Another example: run an LLM locally

You can run many models using Ollama:

`docker run --rm -d -v /my/home/model/path:/root/.ollama -p 11434:11434 --name ollama -it ollama/ollama`

then open a shell to chat with it:

`docker exec -it ollama ollama run llama3.2`

The same instance can be used via the Python library, connecting to the
 port 11434.

---



# Motions

Motion animations are powered by [@vueuse/motion](https://motion.vueuse.org/), triggered by `v-motion` directive.

```html
<div
  v-motion
  :initial="{ x: -80 }"
  :enter="{ x: 0 }"
  :click-3="{ x: 80 }"
  :leave="{ x: 1000 }"
>
  Slidev
</div>
```

<div class="w-60 relative">
  <div class="relative w-40 h-40">
    <img
      v-motion
      :initial="{ x: 800, y: -100, scale: 1.5, rotate: -50 }"
      :enter="final"
      class="absolute inset-0"
      src="https://sli.dev/logo-square.png"
      alt=""
    />
    <img
      v-motion
      :initial="{ y: 500, x: -100, scale: 2 }"
      :enter="final"
      class="absolute inset-0"
      src="https://sli.dev/logo-circle.png"
      alt=""
    />
    <img
      v-motion
      :initial="{ x: 600, y: 400, scale: 2, rotate: 100 }"
      :enter="final"
      class="absolute inset-0"
      src="https://sli.dev/logo-triangle.png"
      alt=""
    />
  </div>

  <div
    class="text-5xl absolute top-14 left-40 text-[#2B90B6] -z-1"
    v-motion
    :initial="{ x: -80, opacity: 0}"
    :enter="{ x: 0, opacity: 1, transition: { delay: 2000, duration: 1000 } }">
    Slidev
  </div>
</div>

<!-- vue script setup scripts can be directly used in markdown, and will only affects current page -->
<script setup lang="ts">
const final = {
  x: 0,
  y: 0,
  rotate: 0,
  scale: 1,
  transition: {
    type: 'spring',
    damping: 10,
    stiffness: 20,
    mass: 2
  }
}
</script>

<div
  v-motion
  :initial="{ x:35, y: 30, opacity: 0}"
  :enter="{ y: 0, opacity: 1, transition: { delay: 3500 } }">

[Learn more](https://sli.dev/guide/animations.html#motion)

</div>

---

# LaTeX

LaTeX is supported out-of-box. Powered by [KaTeX](https://katex.org/).

<div h-3 />

Inline $\sqrt{3x-1}+(1+x)^2$

Block
$$ {1|3|all}
\begin{aligned}
\nabla \cdot \vec{E} &= \frac{\rho}{\varepsilon_0} \\
\nabla \cdot \vec{B} &= 0 \\
\nabla \times \vec{E} &= -\frac{\partial\vec{B}}{\partial t} \\
\nabla \times \vec{B} &= \mu_0\vec{J} + \mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t}
\end{aligned}
$$

[Learn more](https://sli.dev/features/latex)

---

# Diagrams

You can create diagrams / graphs from textual descriptions, directly in your Markdown.

<div class="grid grid-cols-4 gap-5 pt-4 -mb-6">

```mermaid {scale: 0.5, alt: 'A simple sequence diagram'}
sequenceDiagram
    Alice->John: Hello John, how are you?
    Note over Alice,John: A typical interaction
```

```mermaid {theme: 'neutral', scale: 0.8}
graph TD
B[Text] --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```

```mermaid
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid
```

```plantuml {scale: 0.7}
@startuml

package "Some Group" {
  HTTP - [First Component]
  [Another Component]
}

node "Other Groups" {
  FTP - [Second Component]
  [First Component] --> FTP
}

cloud {
  [Example 1]
}

database "MySql" {
  folder "This is my folder" {
    [Folder 3]
  }
  frame "Foo" {
    [Frame 4]
  }
}

[Another Component] --> [Example 1]
[Example 1] --> [Folder 3]
[Folder 3] --> [Frame 4]

@enduml
```

</div>

Learn more: [Mermaid Diagrams](https://sli.dev/features/mermaid) and [PlantUML Diagrams](https://sli.dev/features/plantuml)

---
foo: bar
dragPos:
  square: 0,-231,0,0
---

# Draggable Elements

Double-click on the draggable elements to edit their positions.

<br>

###### Directive Usage

```md
<img v-drag="'square'" src="https://sli.dev/logo.png">
```

<br>

###### Component Usage

```md
<v-drag text-3xl>
  <carbon:arrow-up />
  Use the `v-drag` component to have a draggable container!
</v-drag>
```

<v-drag pos="663,206,261,_,-15">
  <div text-center text-3xl border border-main rounded>
    Double-click me!
  </div>
</v-drag>

<img v-drag="'square'" src="https://sli.dev/logo.png">

###### Draggable Arrow

```md
<v-drag-arrow two-way />
```

<v-drag-arrow pos="67,452,253,46" two-way op70 />

---
src: ./pages/imported-slides.md
hide: false
---

---

# Monaco Editor

Slidev provides built-in Monaco Editor support.

Add `{monaco}` to the code block to turn it into an editor:

```ts {monaco}
import { ref } from 'vue'
import { emptyArray } from './external'

const arr = ref(emptyArray(10))
```

Use `{monaco-run}` to create an editor that can execute the code directly in the slide:

```ts {monaco-run}
import { version } from 'vue'
import { emptyArray, sayHello } from './external'

sayHello()
console.log(`vue ${version}`)
console.log(emptyArray<number>(10).reduce(fib => [...fib, fib.at(-1)! + fib.at(-2)!], [1, 1]))
```

---
layout: center
class: text-center
---

# Learn More

[Documentation](https://sli.dev) · [GitHub](https://github.com/slidevjs/slidev) · [Showcases](https://sli.dev/resources/showcases)

<PoweredBySlidev mt-10 />
