# Python-20220216--Adrian-Diaz-Garcia

This project will ping some websites and will try to match a regex in its content (html).
Results will be sent to a Kafka topic and after to a postgresql database.

<div align="center">

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)]((https://github.com/GregAiven/Python-20220216--Adrian-Diaz-Garcia/))
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Python-20220216--Adrian-Diaz-Garcia

</div>

## ⚙ Architectural design

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="681px" viewBox="-0.5 -0.5 681 241" content="&lt;mxfile host=&quot;app.diagrams.net&quot; modified=&quot;2022-02-21T12:14:18.719Z&quot; agent=&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36&quot; etag=&quot;Aszf2jSQrcpT66UMtG52&quot; version=&quot;16.6.1&quot; type=&quot;device&quot;&gt;&lt;diagram id=&quot;Vzru966eHNFxHBskvHuk&quot; name=&quot;Page-1&quot;&gt;1VjbcpswFPwaPybDxQb8GF+azsSZZsbttH2UQQYlMmKEiI2/vkdI3CI7dSYXJy82WoSQdvesgIE73eyuOcqSWxZhOnCsaDdwZwPHsYeOB38SKRXie4ECYk4i3akFlmSPNWhptCARznsdBWNUkKwPhixNcSh6GOKcbfvd1oz275qhGBvAMkTURH+TSCQKDRy/xb9jEif1nW1vrM5sUN1ZryRPUMS2HcidD9wpZ0yoo81uiqkkr+ZFXfftyNlmYhyn4pQL2MOvfTr0xhezkX11fzPZ30wmF64a5RHRQi94KZDIJXlpBL8cx3inVhMmeh2irMnBEXClm4yLhMUsRXTeohPOijTCcgYWtNo+C8YyAG0A77EQpRYeFYIBlIgN1Wdhcbz8I6+/dEZ1+2/VDvwGmO30HVSr7LbuMCcbLDDXoFqFnPpRIjWUs4KH+Bn2akMiHmPxTD+nkRvqBDOYDS8rcikS5LE/D6QNGzf99KVXnKOy0yFjJJVKNSPfSQA61LXna+OVtTV7/oADNWLd6kythSoPvcBPo3N45AyKDl+paEeFl5PsmUWL00gWLUuxLFac5zLWHI/CGiYrDkexPMqgCBxri1c5EfigUgu0ggDvsYsoiVM4DoFMWUSTR8wFgYS80ic2JIqUkDgne7SqxpNSaofC4KPJYDRrlJID4F2PIx3f+uI2NLsaHjecKYQe/cK6tGVMVGO9rNzaeqq7sPU6B1M8Ve8NqsY2BL1lKRGMGxr1a2WbgI7LDFWW3sIGfKguDrBtVMZRAsf9DGl02bZ7oV1jSWcf9Kx38r5jUPUb7Gx6mVJ4QpCmhG03k2BIWRF9CGeO2ydteCJnwXtxFnzxUB6eGMr+OUN5bBhzytK8gCxuE/mAT79i5gbP2h8e1Hr2d1+XvnWSO0+q4/3SeGgoeYPWD6h688hIePZMdoPPFsq2uYEtYffClex5QasXCpLCz921fBdcffFA8k8MJNs6LOTHJJJviDL/uTi7e73Rp3OvZRBlsNQ8RZSUAF3c/T9XK0XsYtUAKHyIK7p/FAKGwRrPlWPt0RsR/CQePJNf722ePqDZfr5Q6dt+BHLn/wA=&lt;/diagram&gt;&lt;/mxfile&gt;" onclick="(function(svg){var src=window.event.target||window.event.srcElement;while (src!=null&amp;&amp;src.nodeName.toLowerCase()!='a'){src=src.parentNode;}if(src==null){if(svg.wnd!=null&amp;&amp;!svg.wnd.closed){svg.wnd.focus();}else{var r=function(evt){if(evt.data=='ready'&amp;&amp;evt.source==svg.wnd){svg.wnd.postMessage(decodeURIComponent(svg.getAttribute('content')),'*');window.removeEventListener('message',r);}};window.addEventListener('message',r);svg.wnd=window.open('https://viewer.diagrams.net/?client=1&amp;page=0&amp;edit=_blank');}}})(this);" style="cursor:pointer;max-width:100%;max-height:241px;"><defs/><g><path d="M 80 180 L 80 70 L 163.63 70" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 168.88 70 L 161.88 73.5 L 163.63 70 L 161.88 66.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 80px; margin-left: 80px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">Stats and regex match</div></div></div></foreignObject><text x="80" y="83" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">Stats and regex match</text></switch></g><path d="M 120 210 L 283.63 210" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 288.88 210 L 281.88 213.5 L 283.63 210 L 281.88 206.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 211px; margin-left: 190px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">Sends one message<br />per website</div></div></div></foreignObject><text x="190" y="214" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">Sends one message...</text></switch></g><rect x="0" y="180" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 210px; margin-left: 1px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">Monitor</div></div></div></foreignObject><text x="60" y="214" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">Monitor</text></switch></g><path d="M 170 20 C 146 20 140 40 159.2 44 C 140 52.8 161.6 72 177.2 64 C 188 80 224 80 236 64 C 260 64 260 48 245 40 C 260 24 236 8 215 16 C 200 4 176 4 170 20 Z" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 40px; margin-left: 141px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">Webs</div></div></div></foreignObject><text x="200" y="44" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">Webs</text></switch></g><path d="M 410 210 L 553.63 210" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 558.88 210 L 551.88 213.5 L 553.63 210 L 551.88 206.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 208px; margin-left: 481px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">Consumes messages</div></div></div></foreignObject><text x="481" y="211" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">Consumes messages</text></switch></g><rect x="290" y="180" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 210px; margin-left: 291px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">Kafka topic</div></div></div></foreignObject><text x="350" y="214" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">Kafka topic</text></switch></g><path d="M 620 180 L 620 106.37" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 620 101.12 L 623.5 108.12 L 620 106.37 L 616.5 108.12 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 140px; margin-left: 620px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">Store results in PG db</div></div></div></foreignObject><text x="620" y="143" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">Store results in PG db</text></switch></g><rect x="560" y="180" width="120" height="60" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 210px; margin-left: 561px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">ETL</div></div></div></foreignObject><text x="620" y="214" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">ETL</text></switch></g><path d="M 590 35 C 590 26.72 603.43 20 620 20 C 627.96 20 635.59 21.58 641.21 24.39 C 646.84 27.21 650 31.02 650 35 L 650 85 C 650 93.28 636.57 100 620 100 C 603.43 100 590 93.28 590 85 Z" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 650 35 C 650 43.28 636.57 50 620 50 C 603.43 50 590 43.28 590 35" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.diagrams.net/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>

### Monitor

Monitor component will iterate over the websites defined in settings.py file, make a request a match the pattern provided
Format of the website structure is:

```python
# Configure here urls and patterns to search on the webs
WEBS = [
    {"url": "https://www.google.es/", "pattern": r"search"},
    {"url": "https://www.google.es/", "pattern": r"look"},
    {"url": "https://www.google.es/", "pattern": r"wat"},
    {"url": "https://www.amazon.es/", "pattern": r"Prime"},
    {"url": "https://www.amazon.es/", "pattern": r"Adrian"},
]
```

The different fields that monitor will generate are:

- *http_status*: HTTP status request status
- *check_result*: True if regex was found in the content, False otherwise
- *elapsed*: Time in seconds the request took to complete
- *regex*: Regex used to assert in the content
- *url*: Requested URL

Once those stats are collected, they are pushed to a Kafka topic (default: web_checks) to be consumed by the ETL component.

### ETL

ETL component is in charge of consuming the messaged generated by the Monitor component and storing them into a PostgreSQL

### PostgreSQL 

Currently this implementation only uses one table called "check_results" under the public schema.
The table creation statement is 

```sql
CREATE TABLE IF NOT EXISTS public.check_results (
    id SERIAL PRIMARY KEY,
    url text NOT NULL,
    regex text NOT NULL,
    http_status integer NOT NULL,
    check_result boolean NOT NULL,
    elapsed float NOT NULL,
    created TIMESTAMPTZ DEFAULT Now());
```

Under scripts folder there is an initdb.sh script which is taking care of the creation of the table (as in this project no ORM has been used).


## ⚙ Features

### Development features

- Supports for `Python 3.9` and higher.
- [`Pip`](https://pypi.org/project/pip/) as the dependencies manager, requirements can be found in requirements.txt file.
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort).
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).

### Open source community features

- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).


## 🚀 Quick start

> Note: to see more details to execute tests, linting and other extras, see `Makefile usage` section

In order to build and execute the example main program (a.k.a. start monitor some websites defined in settings.py inside the monitor package ):

```
make build
make up
```

### How to configure regex and websites

Edit file in [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort).

> Requirements: you must have docker installed and running
> 
## 🖖Makefile usage

[`Makefile`](https://github.com/GregAiven/Python-20220216--Adrian-Diaz-Garcia/blob/master/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Building local images</summary>
<p>

```bash
make build
```

</p>
</details>

<details>
<summary>2. Tests</summary>
<p>

Running tests inside docker containers using pytest:

```bash
make test
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `isort` and `black`.

```bash
make black isort
```

Codestyle rewrite files and format them:


> Note: `check-codestyle` uses `isort`, `black` library
</details>

<details>
<summary>4. Linters</summary>
<p>

Current used linter is flake8

```bash
make flake8
```
</details>

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |



## 🛡 License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/GregAiven/Python-20220216--Adrian-Diaz-Garcia/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{Python-20220216--Adrian-Diaz-Garcia,
  author = {Adrian Diaz},
  title = {Python-20220216--Adrian-Diaz-Garcia},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/GregAiven/Python-20220216--Adrian-Diaz-Garcia}}
}
```