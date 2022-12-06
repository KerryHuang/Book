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

<iframe id="aswift_0" name="aswift_0" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="696" height="400" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-5143258973069156&amp;output=html&amp;h=400&amp;adk=4109956860&amp;adf=2237193853&amp;w=696&amp;lmt=1663924687&amp;rafmt=12&amp;psa=0&amp;channel=4973241802&amp;format=696x400&amp;url=https%3A%2F%2Fcomputingforgeeks.com%2Finstall-and-configure-iis-web-server-on-windows-server%2F&amp;wgl=1&amp;dt=1663924685406&amp;bpp=5&amp;bdt=2684&amp;idt=1621&amp;shv=r20220921&amp;mjsv=m202209080101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;correlator=616593088435&amp;frm=20&amp;pv=2&amp;ga_vid=572647760.1663924687&amp;ga_sid=1663924687&amp;ga_hid=1209513357&amp;ga_fc=1&amp;u_tz=480&amp;u_his=5&amp;u_h=900&amp;u_w=1440&amp;u_ah=875&amp;u_aw=1387&amp;u_cd=24&amp;u_sd=2&amp;adx=158&amp;ady=2442&amp;biw=1384&amp;bih=795&amp;scr_x=0&amp;scr_y=278&amp;eid=44759876%2C44759927%2C44759837%2C44767668%2C42531705&amp;oid=2&amp;pvsid=880810557459152&amp;tmod=1910749240&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.google.com%2F&amp;eae=0&amp;fc=896&amp;brdim=-3%2C25%2C-3%2C25%2C1387%2C25%2C1384%2C875%2C1384%2C795&amp;vis=1&amp;rsz=%7C%7CoeEbr%7C&amp;abl=CS&amp;pfx=0&amp;fu=256&amp;bc=31&amp;ifi=1&amp;uci=a!1&amp;btvi=1&amp;fsb=1&amp;xpc=gs0y85RZ8q&amp;p=https%3A//computingforgeeks.com&amp;dtd=1645" data-google-container-id="a!1" data-google-query-id="CLWlkcHKqvoCFVGD6QUdm3EEKA" data-load-complete="true" style="box-sizing: border-box; max-width: 100%; left: 0px; position: absolute; top: 0px; border: 0px; width: 696px; height: 400px;"></iframe>



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