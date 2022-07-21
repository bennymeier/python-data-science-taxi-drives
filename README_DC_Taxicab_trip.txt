TITLE: Taxicab Trip Information

ABSTRACT:  DC Taxi trips from January 2015 to June 2019.  The zip file contains zip files of pipe (|) delimeted text files for trips by month.  The record counts are:

Month			Count
5/2015		1,397,102 
6/2015		1,470,466 
7/2015		1,401,792 
8/2015		1,129,707 
9/2015		1,308,445 
10/2015		1,487,133 
11/2015	 	  993,502 
12/2015		1,081,726 
1/2016	 	  922,338 
2/2016		1,194,698 
3/2016		1,404,639 
4/2016		1,369,882 
5/2016		1,323,155 
6/2016		1,282,651 
7/2016		1,109,118 
8/2016		  949,650 
9/2016		1,203,388 
10/2016		1,027,036 
11/2016		1,011,673 
12/2016	 	  898,993 
1/2017	  	  901,807 
2/2017	 	  949,578 
3/2017		1,237,621
4/2017		1,185,859
5/2017		1,188,944
6/2017		1,182,526
7/2017		  993,834
8/2017     	  813,513
9/2017		  902,795
10/2017    	1,056,864
11/2017    	  867,709
12/2017    	  730,679
1/2018     	  686,993
2/2018     	  750,363
3/2018     	  999,048
4/2018     	1,040,147
5/2018     	  984,593
6/2018     	  941,608
7/2018     	  810,292
8/2018     	  735,262
9/2018    	  819,233
10/2018     	  900,574
11/2018     	  753,670
12/2018     	  670,970
01/2019     	  589,475
02/2019     	  667,546
03/2019     	  902,382
04/2019     	  853,950
05/2019     	  865,374
06/2019    	  800,030


DISCLAIMER: This work is licensed under a Creative Commons Attribution 4.0 International License.

CATEGORY: Public Service	

PROVIDER: Office of the Chief Technology Officer (OCTO)

ORIGINATOR: Department of For-Hire Vehicles (DFHV)

PROCESS DESCRIPTION: DFHV provided OCTO with a taxicab trip text file representing trips from January 2015 to June 2019.  OCTO processed the data to assign a block locations to pick up and drop off locations.  The blocks were assigned using the original pick up, drop off lat/long coordinates and searching for the block locations in the DC Master Address Repository (radius tolerance of 250 meters and less).  The pick and drop off times were also rounded to the nearest hour.

In addition, the pick up and drop off locations were assigned to an airport using locator polygons for Reagan, BWI, and Dulles.  These polygons generally followed the visual borders of these airports.

The block assignment metrics are as follows
 
					Pick Up Location	    Drop Off Location	   
Total Records (overall):		53,173,692			53,173,692
Percent Geocoded to block:		82%	             		 75%	    
			 
For more information, go to http://dfhv.dc.gov

TABLE STRUCTURE:	 

COLUMN_NAME		DATA_TYPE		DESCRIPTION
OBJECTID			NUMBER(9)		Table Unique Identifier	
TRIPTYPE			VARCHAR2(255)	Type of Taxi Trip
PROVIDERNAME		VARCHAR2(255)	Taxi Company that Provided 								trip	
FAREAMOUNT			VARCHAR2(255)	Meter Fare Amount
GRATUITYAMOUNT		VARCHAR2(255)	Tip amount
SURCHARGEAMOUNT		VARCHAR2(255)	Surcharge fee
EXTRAFAREAMOUNT		VARCHAR2(255)	Extra fees
TOLLAMOUNT			VARCHAR2(255)	Toll amount
TOTALAMOUNT		VARCHAR2(255)	Total amount from Meter 								fare, tip, surcharge, 								extras, and tolls. 
PAYMENTTYPE		VARCHAR2(255)	Payment type
ORIGINCITY			VARCHAR2(255)	Pick up location city
ORIGINSTATE		VARCHAR2(255)	Pick up location state
ORIGINZIP			VARCHAR2(255)	Pick up location zip
DESTINATIONCITY		VARCHAR2(255)	Drop off location city
DESTINATIONSTATE		VARCHAR2(255)	Drop off location state
DESTINATIONZIP		VARCHAR2(255)	Drop off location zip
MILEAGE			VARCHAR2(255)	Trip milaege
DURATION			VARCHAR2(255)	Trip time - duration of 								travel
ORIGIN_BLOCK_LATITUDE	NUMBER		Pick up location latitude
ORIGIN_BLOCK_LONGITUDE/NUMBER		Pick up location longitude
ORIGIN_BLOCKNAME		VARCHAR2(255)	Pick up location street 								block name
DESTINATION_BLOCK_LAT	NUMBER		Drop off location latitude
DESTINATION_BLOCK_LONGNUMBER		Drop off location longitude
DESTINATION_BLOCKNAME	VARCHAR2(255)	Drop off location street 								block name
AIRPORT			CHAR(1)		Pick up or drop off 									location is a local airport 							(Y/N)
ORIGINDATETIME_TR	DATE			Pick up date and time	
DESTINATIONDATETIME_TRDATE			Drop off date and time	


Payment Type
1.	Credit
2.	Cash
3.	EHail 
4.	Other (not sure how common this is)
5.	Uber (not sure how common this is)
Trip Type
1.	Ordinal (normal rate)
2.	VoD 
3.	TransportDC (grant program)
4.	TransportDCShared (grant program)
5.	MOVA (grant program)
6.	CFSA (grant program)
7.	NRS (grant program)
8.	NEMT (grant program


