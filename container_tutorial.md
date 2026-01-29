steps to create container for editing bitaxe firmware. totally will forget after like a week :D

1.	$ `cd firmware_root/`

2.	build the docker with image for ESP: $ `docker build --no-cache -t esp-idf-qemu -f .devcontainer/Dockerfile .`

3.	run the docker with imported /workspaces: $ `docker run -it --privileged -v "$(pwd):/workspaces" esp-idf-qemu:latest`

output: ```... Done! You can now compile ESP-IDF projects.
Go to the project directory and run: idf.py build```

4.	if missing java ($ `java -version`), run: $ `cd; apt-get update; apt-get install -y default-jre`

5.	trust the docker $ `cd; git config --global --add safe.directory /workspaces`

6. 	root@3ae5393b06b6:/# `cd /workspaces; . /opt/esp/idf/export.sh`

7.	root@3ae5393b06b6:/# `idf.py fullclean; idf.py build`

8.	create the .bin firmware root@3ae5393b06b6:/workspaces# `./merge_bin.sh ./esp-miner-merged.bin`

build new version: $ `idf.py build; ./merge_bin.sh ./esp-miner-merged.bin`
