# allViral
determine a viral information

## Deploy

**Scrapyd** is an application (typically run as a daemon) that listens to requests for spiders to run and spawns a process for each one
For more information refer to [scrapyd documentation](https://scrapyd.readthedocs.io/en/latest/index.html)

### Install scrapyd
`pip install scrapyd`


### Run scrapy daemon
`scrapyd`

### Check it
in the browser >http://localhost:6800/


### Install scrapyd-client
`pip install scrapyd-client`


### Run deploy
in another terminal tab run:  
`scrapyd-deploy default`


### Launch a spider
`curl http://localhost:6800/schedule.json -d project=project -d spider=somespider`
> e.g:  
`curl http://localhost:6800/schedule.json -d project=allViral -d spider=techcrunch -d setting=FEED_URI=file:///home/edouard/Desktop/allViral/output.json`




