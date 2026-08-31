---
publish: "false"
---

- Vamos a usar el plugin __Quartz Syncer__
- Para instalarlo, primero instalamos __BRAT__ Plugin 
- Desde el plugin, le damos la dirección del __Quartz Syncer__:  `saberzero1/quartz-syncer`
- Seguimos las instrucciones de la [Setup-Guide](https://saberzero1.github.io/quartz-syncer-docs/setup-guide)
	- Prerequisitos
		- `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash`
		- `source ~/.bashrc`
		- `nvm install 22`
		- `nvm alias default 22`
	- Quartz
		- `https://github.com/new?template_name=quartz&template_owner=jackyzha0`
			- esto abre una página en la que inicio mi repositorio  wpregliasco/python-sci
		- lo clonamos a Projects/pages/python-sci
		- `cd ...`
		- `npm ci`
		- tuve un conflicto de versiones y las aprobé a lo bestia
			- `npm install-scripts approve @parcel/watcher esbuild sharp`
		- Creamos el repositorio Quartz:
			- `npx quartz create`
				- template: Obsidian
				- empty
				- base-url: wpregliasco/python-sci
		- Chequeamos si funciona: `npx quartz build --serve`
		  
	
![](https://prod-images.merino.prod.webservices.mozgcp.net/wikimedia_potd/2026-08-30/thumbnail.jpeg)