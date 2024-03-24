# Web Scraping with Tor Proxy

This script is designed to scrape URLs using Tor proxies for anonymity. It checks the Tor connection, reads URLs from a file, and then scrapes each URL concurrently using multithreading.

## Features

- Checks Tor connection to ensure anonymity.
- Reads URLs from a specified file.
- Scrapes each URL concurrently for efficient processing.
- Logs activity to a log file for tracking.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` library
- Tor service running locally

## Installation

1. Clone this repository to your local machine
2. Install the required Python libraries
3. Ensure Tor service is running locally on default port `127.0.0.1:1337`.

## Usage

1. Ensure Tor service is running locally.
2. Prepare a file containing a list of URLs to scrape, with each URL on a new line.
3. Run the script
4. Follow the prompts, providing the file path containing URLs when prompted.

## Configuration

- Modify the `proxies` dictionary in the `main` function to match your Tor configuration if it differs.
- Adjust the `max_workers` parameter in `ThreadPoolExecutor` to control the number of concurrent scraping threads.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Stores

GammaGoblin - http://mb2lgz7zknnuf77qpdgxdlon65idlv6htwgxqd6esy545frhjzoi6nad.onion

SmokersCo - http://cxhxevjctgurhvdarbtibo7eikwcu7fkudytiiqegjezvdydiowshgqd.onion

Pygmalion Store - http://7q25kbaw2rxouxjchvtcr74km4mqxqkp44nwbqwppzig4v5d4nbit4ad.onion

The Spitzenkörper - http://d4giq7x7ptke7mwepvjmeqlael3nf7vlib5psxi5smsmh4uoxlj4gfyd.onion

Tribe Seuss - http://eisrgs2qjiuvof4qvch2yknfq2m6ha4qyipgvggepjaseorh4bhykiqd.onion


Established Darknet markets

Incognito Market - http://incognirnybkn24z7uxkru5f7esi7jvqw72qtnhkq3koztw4fkl5emyd.onion

MGM Grand Market - http://duysanjcemitm4r6sadiqzkswvx6kx7vxur4sycuocrzrekutpb3d5qd.onion

DrugHub Market - http://drughubmgeg6mt2cebp7b5aknd7iqlwnhfxg6tketey2234ubzqkucid.onion

Go Fish Market - http://gofish4mxkyvdjncmyfm4paptmg4gyatqg7hay3y4kyzzjmw3jarcsyd.onion

Abacus Market - http://abacuseg5vlppx3afutoh4msztikn7gcfr4rud3ofemjvzqtx4256xid.onion

Nemesis Market - http://zjaibnwx4lykbsxhvd2tllhqinpkfgmiuwirqepswutth77fuhl67qad.onion

Kerberos Market - http://kerberoxl2y6mtsxcr5fiffoodu4nvbtnukshtgmexnjareza7uwh2qd.onion

Ares Market - http://sn2sfdeyluqqdjehgky4ua72cmklsjng2sbfm3difrnsyvtgewkfq6qd.onion

Super Market - http://superxx2a6dn5hjuewfcpt6ko3h2jvmc4kuq7jtztg7hdxq64cmowyyd.onion

Cypher Market - http://6c5qaelgldw6ktl7lkfv2d432qoyo7j7kd22hebwlbx7khpvitb4t4id.onion

Archetyp Market - http://arche65jhbxenremkwwwpy2ulo2zdhbr3jtykqh65igcw6hfpzpdgkyd.onion

Drugula Market - http://drugula2p4n2xxjjr6goeupgipkdiztemvxdkdx4ds75f5ijj4w27syd.onion

Dark Matter Market - http://darkmatile7wd5oi655lpbsco5nziq43kdb75nxbcqt3h64rany6evad.onion

Kingdom Market - http://kingdomnf4eyeacbzpsrhjna5xiksnp6ddxhskuj6gyvbb3kzteydqid.onion

We The North Market (Canada) - http://hn2paw7xssgi667hb2ip335q2t6x236kcoedsanyj6jicpq2wb66i5qd.onion

Flugsvamp 4.0 (Sweden) - http://fs4is7s64kbow5w37kkptu2zmlw5ahjeagmtrgfdtwet3burwqvcciad.onion

BlackSprut Market (Russia) - http://btrhbfqli73vj4x5nspknftmlmbfeclncpah4rafytwh3akbofqakwid.onion

Mega Market (Russia) - http://mega555la2l35altkhky65cuoks3escuxd7qyveozy5gtm2a4w5eu7qd.onion

Ramp Market (Russia) - http://rampclum7j4vgz54i6p63eahkr5wsyq7rwbxgclx4ag3estqwovfasqd.onion

Nexus Market - http://nexusaohrt72l2i5crrmyhk3em3dcd33rewmbkwit3roc3maj36znhqd.onion


Crypto Exchanges

Exch Exchange - http://hszyoqrkjqja7ieobhmeo3zarssqp4yvrtszvdxx3pevy6u3otuh4mad.onion

Swp.Cx - http://uicrmr3rtckrm3fh3knuvquhrhp5qvlpku7iyf3jttmgo6jpunu6rrad.onion

Xchange.me - http://xmxmrjwhh66fgn32cwi6qylqqsjh4dqj6mutrjxz4vqh4h5ipdifirqd.onion

Infinity Exchanger - http://exchanger.dhme3vnfeleniirt5nxuhpmjsfq5srp44uyq2jyihhnrxus7ibfqhiqd.onion


**For educational purposes only:** This project is designed for educational purposes related to web scraping. Unauthorized or unlawful web scraping activities are prohibited. It is the user's responsibility to comply with the terms of use of any website and obtain permission before scraping.
