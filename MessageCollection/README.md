# Message collection

## Introduction

Messages are sent thru HTTPS to Event Hubs. 

Event Hubs can store data to blob storage (not used here). It can also be read by services like Azure Stream Analytics.
Azure Stream Analytics can then send data to [Power BI](http://powerbi.com).

## from the robot to Power BI

The following has been put in place:

- the robot sends data to Event Hub
    - the robot get a SAS token (here is an example in curl: ![](img/1a.png)) which is given by an Azure function: ![](img/1.png)
        - the function has the event hub management key: ![](img/2.png) ![](img/3.png)
        - the data is sent thru a Web Request too, from unity
            - here is the equivalent in curl: ![](img/4.png)
    - the data is received by Azure Event Hub: ![](img/5.png)
    - it is then processed by Azure Stream Analytics: ![](img/6.png) 
    - Azure Stream Analytics sends ![](img/7.png)
        - a copy of all the data to blob storage ![](img/8.png)
            - the data can be searched with Azure Stream Analytics: ![](img/10.png) ![](img/11.png) ![](img/12.png)  
        - a summary of the data to Power BI ![](img/9.png)
