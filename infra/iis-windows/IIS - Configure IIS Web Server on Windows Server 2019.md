---
kind: reprint
source: site:computingforgeeks.com
---

# Configure IIS Web Server on Windows Server 2019

## Introduction

According to [Microsoft Docs](https://docs.microsoft.com/), the Web Server (IIS) role in Windows Server 2019 provides a secure, easy-to-manage, modular and extensible platform for reliably hosting websites, services, and applications. The new release of Windows Server 2019 from Microsoft comes with IIS version 10. This guide shows how it is installed and how various activities such as the creation of websites, Virtual directories, and others are tackled. We shall begin by installing IIS.

## Step 1: Start Server Manager

As with all Windows Server roles, we have to go to the Server Manager to begin the installation. Hit your “**Windows**” key and search for **Server Manager** if it is not already opened. Once open, click on “**Add Roles and Features**“

[![Server Manager start](https://computingforgeeks.com/wp-content/uploads/2019/10/Server_Manager_start.png?ezimgfmt=rs:696x378/rscb23/ng:webp/ngcb23)](https://computingforgeeks.com/wp-content/uploads/2019/10/Server_Manager_start.png?ezimgfmt=rs:696x378/rscb23/ng:webp/ngcb23)

[![Add Roles and Features Dashboard](https://computingforgeeks.com/wp-content/uploads/2019/10/Add_Roles_and_Features_Dashboard.png?ezimgfmt=rs%3Adevice%2Frscb23-1)](https://computingforgeeks.com/wp-content/uploads/2019/10/Add_Roles_and_Features_Dashboard.png?ezimgfmt=rs%3Adevice%2Frscb23-1)

## Step 2: Click Next on Wizard

On the first page of the “**Add Roles and Features Wizard**“, click “**Next**“

[![Add Roles and Features First Part 1](https://computingforgeeks.com/wp-content/uploads/2019/10/Add_Roles_and_Features_First_Part-1-1024x729.png?ezimgfmt=rs:696x495/rscb23/ng:webp/ngcb23)](https://computingforgeeks.com/wp-content/uploads/2019/10/Add_Roles_and_Features_First_Part-1-1024x729.png?ezimgfmt=rs:696x495/rscb23/ng:webp/ngcb23)

## Step 3: Select Installation Type

In the “**Select Installation type page**“, select “**Role-based or feature-based-installation**” and click “**Next**“


[![Add Roles and Features POP Role based 1](https://computingforgeeks.com/wp-content/uploads/2019/10/Add_Roles_and_Features_POP_Role_based-1-1024x733.png?ezimgfmt=rs:696x498/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

## Step 4: Choose Destination Server

Select the server you will install NFS on and click “**Next**“



[![Select server new](https://computingforgeeks.com/wp-content/uploads/2019/10/Select_server_new-1024x727.png?ezimgfmt=rs:696x494/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

## Step 5: Select Roles to install

In this “**Select server roles**” part check the “**WebServer (IIS)**” box then a pop-up window will come up.

[![iis select Web server iis](https://computingforgeeks.com/wp-content/uploads/2019/10/iis_select-Web-server-iis-1024x733.png)](https://computingforgeeks.com/wp-content/uploads/2019/10/iis_select-Web-server-iis-1024x733.png)

## Step 6: Add IIS Features

In the pop-up window, just click on “**Add Features**” then hit “**Next**“. After that click “**Next**” on the next three consecutive windows as illustrated below.

[![IIS Add Features](https://computingforgeeks.com/wp-content/uploads/2019/10/IIS_Add_Features.png?ezimgfmt=rs:696x684/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

[![IIS Add Features Next](https://computingforgeeks.com/wp-content/uploads/2019/10/IIS_Add_Features_Next-1024x733.png?ezimgfmt=rs:696x498/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

[![IIS Add Features Next 2](https://computingforgeeks.com/wp-content/uploads/2019/10/IIS_Add_Features_Next-2-1024x733.png?ezimgfmt=rs:696x498/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

[![IIS Add Features Next 3](https://computingforgeeks.com/wp-content/uploads/2019/10/IIS_Add_Features_Next-3-1024x733.png?ezimgfmt=rs:696x498/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

## Step 7: Confirm Selections

On the “**Confirm installation selections**” page simply click on “**Install**” and afford it some time to finish after which you just click “**Close**“.



[![iis confirm selections and install](https://computingforgeeks.com/wp-content/uploads/2019/10/iis-confirm-selections-and-install-1024x730.png?ezimgfmt=rs:696x496/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

[![iis installation success and close](https://computingforgeeks.com/wp-content/uploads/2019/10/iis-installation-success-and-close-1024x730.png?ezimgfmt=rs:696x496/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

## Step 8: Prove the Web Server is running

Open your browser either within the server or on a computer that can access your IIS Server network and input its IP Address on the browser’s search as shown below. If it loads, then we are good to go.



[![iis server on browser](https://blog.hungwin.com.tw/wp-content/uploads/2021/07/windows-server-iis-install-16.png)](data:image/svg+xml,)

## Step 9: Configure Default Site

Use our guide below to configure a default website on IIS Server 2019.

- How To Configure Default Site in IIS Server 2019

  


## Conclusion

After we are done installing IIS Webserver, we now have a lot to do such as configuring Virtual Directories, using the default website, Adding Websites, SSL and TLS stuff and much more. Stay tuned.

More on Windows Server:

- [How To Configure Virtual Directory on Windows IIS Server 2019](https://computingforgeeks.com/configure-virtual-directory-on-windows-iis-server/)
- [Install and Configure NFS Server on Windows Server 2019](https://computingforgeeks.com/install-and-configure-nfs-server-on-windows-server/)
- [Install and Configure NFS Client on Windows 10 / Server 2019](https://computingforgeeks.com/install-and-configure-nfs-client-on-windows-10-server-2019/)
- [Configure Windows Client to Obtain IP from DHCP Server](https://computingforgeeks.com/configure-windows-client-to-obtain-ip-from-dhcp-server/)
- [How to run Docker Containers on Windows Server 2019](https://computingforgeeks.com/how-to-run-docker-containers-on-windows-server-2019/)