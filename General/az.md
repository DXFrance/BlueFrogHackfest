# az

When installed, you can start it, check its version and login

```
az

az --version

az login
```

The examples in this repo use the latest docker version

```
docker run -it --rm azuresdk/azure-cli-python
az

az --version
```

which returns

```
bash-4.3# az

     /\
    /  \    _____   _ _ __ ___
   / /\ \  |_  / | | | \'__/ _ \
  / ____ \  / /| |_| | | |  __/
 /_/    \_\/___|\__,_|_|  \___|


Welcome to the cool new Azure CLI!

Here are the base commands:

    account   : Manages stored and default subscriptions.
    acr       : Commands to manage Azure container registries.
    acs       : Manage Azure container services.
    ad        : Synchronize on-premises directories and manage Azure Active Directory (AAD)
                resources.
    appservice: Commands for managing your Azure web apps, app service plans, etc.
    cloud     : Manage the Azure clouds registered.
    component : Manages and updates Azure CLI components.
    configure : Interactive experience for setting up the Azure CLI.
    container : Set up automated builds and deployments for multi-container Docker applications.
    context   : Manage contexts.
    feedback  : Loving or hating the CLI?  Let us know!
    iot       : Connect, monitor, and control millions of IoT assets.
    keyvault  : Safeguard and maintain control of keys, secrets, and certificates.
    login     : Log in to access Azure subscriptions.
    logout    : Log out to remove accesses to Azure subscriptions.
    network   : Manages Network resources.
    provider  : Manage resource providers.
    redis     : Access to a secure, dedicated cache for your Azure applications.
    resource  : Generic commands to manage Azure resources.
    role      : Use role assignments to manage access to your Azure resources.
    storage   : Durable, highly available, and massively scalable cloud storage.
    tag       : Manage resource tags.
    taskhelp  : Provides long-form help content by topic.
    vm        : Provision Linux and Windows virtual machines in minutes.
    vmss      : Create highly available, auto-scalable Linux or Windows virtual machines.
```

```
bash-4.3# az --version
azure-cli (0.1.0b9)

acr (0.1.0b9)
acs (0.1.0b9)
appservice (0.1.0b9)
cloud (0.1.0b9)
component (0.1.0b9)
configure (0.1.0b9)
container (0.1.0b9)
context (0.1.0b9)
core (0.1.0b9)
feedback (0.1.0b9)
iot (0.1.0b9)
keyvault (0.1.0b9)
network (0.1.0b9)
profile (0.1.0b9)
redis (0.1.0b9)
resource (0.1.0b9)
role (0.1.0b9)
storage (0.1.0b9)
taskhelp (0.1.0b9)
vm (0.1.0b9)

Python (Linux) 3.5.2 (default, Nov  1 2016, 00:13:39)
[GCC 5.3.0]
bash-4.3#
```

You can configure the way az formats its output with `az configure`
