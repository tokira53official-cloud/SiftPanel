# SiftNodes Custom Hosting Panel

Your Ultimate IT & Hosting Partner

About

SiftNodes is a custom hosting panel inspired by Pterodactyl Panel. It is designed to manage Minecraft servers, Python applications, Node.js applications, Java applications, PHP applications and other supported Docker workloads.

Features

- Custom dark purple and blue dashboard
- Administrator dashboard
- Secure authentication
- Docker-based server management
- Minecraft server management
- Python server management
- Node.js server management
- Java application hosting
- PHP application hosting
- Server start, stop and restart
- Server console and logs
- File manager
- CPU, RAM and disk monitoring
- Server resource limits
- Port allocation
- User management and permissions
- Backup and restore
- Mobile-friendly interface
- Automated installation scripts

Repository Structure

SiftNodes/
|
|-- main.sh
|-- install-panel.sh
|-- install-wings.sh
|-- requirements.txt
|-- README.txt
|
|-- app/
|-- frontend/
|-- backend/
|-- docker/
|-- config/

Requirements

- Ubuntu 22.04 or Ubuntu 24.04
- Root or sudo access
- Internet connection
- Docker Engine
- Python 3
- A domain name for public HTTPS access

Installation

Download or clone the repository onto your server.

Run the main installer:

bash main.sh

The installer should provide separate options for installing the panel and preparing the Docker node.

Panel installation:

bash install-panel.sh

Node installation:

bash install-wings.sh

IMPORTANT:
The node installation script must configure a node service that is compatible with the panel backend. Installing Docker alone does not install Pterodactyl Wings.

Administrator Account

Username: admin

The installer must generate a secure initial password or request one during setup.

Do not use a default password on a public server.

Supported Server Types

Minecraft:

- Paper
- Purpur
- Vanilla
- Fabric
- Forge

Other applications:

- Python
- Node.js
- Java
- PHP
- Static websites
- Approved custom Docker images

Supported runtimes must be configured and tested before production use.

Security

- Use HTTPS for public access.
- Store passwords as secure hashes.
- Keep secrets outside the public repository.
- Restrict administrator access.
- Apply CPU, RAM, disk and process limits.
- Isolate containers from the host.
- Never expose the Docker socket to untrusted users.
- Validate all server creation requests.
- Maintain logs and backups.

Project Status

Development project.

Do not use this starter project for untrusted public workloads until authentication, container isolation, resource limits, file permissions and API security have been reviewed.

License

Choose and add an appropriate open-source license before publishing the project.
