## Why did you build this?
To start, awhile back I deleted my instagram app as I felt it was a time sync and an 
unhealthy distraction from reality. That being said there were a few profiles
I enjoyed that put out some wholesome or funny content (sometimes both). 
I decided to build something to text me updates without me having to 
download yet another app on my phone. I also wanted to be in control of 
any of my data around this process

Also, I wanted to try out a few technologies I had been eyeing. I use redis at
work, but I'd heard great things about Aerospike and wanted a use case.

## Running
**Configurations**
- rename config-example.toml to config.toml
- modify your configuration to the correct values

**Setup python environment**
```shell script
conda create --name=insta-text python=3.7 --file requirements.txt
conda activate insta-text
```

**Setup Aerospike**
```shell script
docker pull aerospike
docker run -d -v <PATH_TO_REPO>/insta-text/aerospike:/opt/aerospike/etc --name aerospike -p 3000:3000 -p 3001:3001 -p 3002:3002 -p 3003:3003 aerospike asd --foreground --config-file /opt/aerospike/etc/aerospike.conf
```

**Run**
```shell script
python -m src.app
```