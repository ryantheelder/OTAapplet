# Installing and Deleting an Applet via OTA SMS
This README.md provides a guide on how to install and delete an applet on a phone using OTA SMS. We explain what an applet is, how OTA SMS works, and the potential risks. You'll find clear instructions on how to use OTA SMS to install and delete applets on your phone.

# System Model
Our system consists of the following components:
- **srsenb**: This component acts as the eNodeB and provides the radio access network (RAN) for our system. It allows mobile devices to connect to our network and communicate with other devices.
- **open5gs**: This component acts as the 4G core network and provides the backbone of our system. It is responsible for authenticating and authorizing devices, managing mobility, and providing connectivity between devices.
- **OsmoMSC**: This component acts as the Short Message Service Center (SMSC) and provides the functionality to send SMS messages over the SGS interface. It is responsible for storing and forwarding messages between devices in the network. OsmoMSC also includes support for SMPP (Short Message Peer-to-Peer) protocol, which allows it to act as an SMPP server. This provides an additional way to send and receive SMS messages from the network.
- **OsmoHLR**: This component acts as the Home Location Register (HLR) and provides the functionality to store and manage subscriber information, such as subscriber profiles, access control information, and service information. It is responsible for maintaining the subscriber database and providing the necessary information to support the network operations.

In LTE networks, SMS messages cannot be sent over the same channels as data traffic due to technical reasons. Therefore, a separate interface known as SGs (SMS Gateway to MSC Server) is used to transfer SMS messages between the mobile device and the SMS center. This is why we are using SGs interface in our system model.

Together, these components provide a powerful and flexible system that allows us to send SMS messages over the SGs interface. By using srsenb, open5gs, and OsmoMSC, we are able to create a reliable and efficient network that meets our needs.

# Steps to Install and Delete an Applet via OTA SMS on a Phone
1. Create an applet: First, you need to create an applet that you want to install on the phone. An applet is a small software program that performs a specific task. For example, you can create an applet that displays a message when the phone is turned on.
2. Convert the applet to a binary file: Once you have created the applet, you need to convert it to a binary file. A binary file is a file that contains executable code that can be run on the phone.
3. Send the binary file via OTA SMS: You can send the binary file to the phone via OTA SMS. OTA SMS stands for Over-The-Air SMS, which is a method of sending SMS messages that contain executable code. The phone will receive the OTA SMS and automatically install the applet.
4. Verify the applet installation: Once the applet has been installed, you can verify that it is working correctly by running it on the phone.
5. Delete the applet: To delete the applet from the phone, you can send another OTA SMS message that contains a command to delete the applet. The phone will receive the OTA SMS and automatically delete the applet.

# Installing the Necessary Software Components
To use our system model and perform the steps described in this README.md file, you will need to install the following software components:
## PreReq
```code
~$ sudo apt update
~$ sudo apt upgrade
~$ sudo apt install libpcsclite-dev libtalloc-dev libortp-dev libsctp-dev libmnl-dev libdbi-dev libdbd-sqlite3 libsqlite3-dev sqlite3 libc-ares-dev
```

## Install UHD
We will be using the USRP B210 software-defined radio (SDR) for our system model, which requires the installation of the Universal Hardware Driver (UHD). UHD is an open-source driver that provides support for a variety of Ettus Research SDRs, including the USRP B210.
To install UHD for use with the USRP B210, please follow the steps below:
```code
~$ sudo apt-get -y install git swig cmake doxygen build-essential libboost-all-dev libtool libusb-1.0-0 libusb-1.0-0-dev libudev-dev libncurses5-dev libfftw3-bin libfftw3-dev libfftw3-doc libcppunit-1.14-0 libcppunit-dev libcppunit-doc ncurses-bin cpufrequtils python-numpy python-numpy-doc python-numpy-dbg python-scipy python-docutils qt4-bin-dbg qt4-default qt4-doc libqt4-dev libqt4-dev-bin python-qt4 python-qt4-dbg python-qt4-dev python-qt4-doc python-qt4-doc libqwt6abi1 libfftw3-bin libfftw3-dev libfftw3-doc ncurses-bin libncurses5 libncurses5-dev libncurses5-dbg libfontconfig1-dev libxrender-dev libpulse-dev swig g++ automake autoconf libtool python-dev libfftw3-dev libcppunit-dev libboost-all-dev libusb-dev libusb-1.0-0-dev fort77 libsdl1.2-dev python-wxgtk3.0 git libqt4-dev python-numpy ccache python-opengl libgsl-dev python-cheetah python-mako python-lxml doxygen qt4-default qt4-dev-tools libusb-1.0-0-dev libqwtplot3d-qt5-dev pyqt4-dev-tools python-qwt5-qt4 cmake git wget libxi-dev gtk2-engines-pixbuf r-base-dev python-tk liborc-0.4-0 liborc-0.4-dev libasound2-dev python-gtk2 libzmq3-dev libzmq5 python-requests python-sphinx libcomedi-dev python-zmq libqwt-dev libqwt6abi1 python-six libgps-dev libgps23 gpsd gpsd-clients python-gps python-setuptools
```

```code
~$ mkdir repos
~$ cd repos
~/repos$ git clone https://github.com/EttusResearch/uhd
~$ cd uhd
~/uhd$ cd host
~/uhd/host$ mkdir build
~/uhd/host$ cd build
~/uhd/host/build$ cmake ..
~/uhd/host/build$ make 
~/uhd/host/build$ sudo make install
~/uhd/host/build$ sudo ldconfig
~/uhd/host/build$ cd ~/repos
```
After installation, test your UHD installation by running the ```~/repos$ sudo uhd_find_devices``` command in your terminal. If your USRP B210 is properly connected, it should be listed in the output.
## **Install srsRAN_4G** 
In addition to the software components we have already discussed, we will also be using srsRAN in our system model. srsRAN is an open-source software-defined radio access network (SD-RAN) platform that provides support for LTE and 5G New Radio (NR) networks.

We will be using srsRAN to provide the LTE radio access network (RAN) component of our system model. srsRAN provides a flexible and scalable LTE RAN solution that can be customized and configured to meet a wide range of use cases and network configurations.

To install srsRAN, you can follow the instructions provided bellow:
```code
~/repos$ sudo apt-get install build-essential cmake libfftw3-dev libmbedtls-dev libboost-program-options-dev libconfig++-dev libsctp-dev
```

```code
~/repos$ git clone https://github.com/srsRAN/srsRAN_4G.git
~/repos$ cd srsRAN_4G
~/repos/srsRAN_4G$ mkdir build
~/repos/srsRAN_4G$ cd build
~/repos/srsRAN_4G/build$ cmake .. 
~/repos/srsRAN_4G/build$ make
~/repos/srsRAN_4G/build$ make test
~/repos/srsRAN_4G/build$ sudo make install
~/repos/srsRAN_4G/build$ srsran_4g_install_configs.sh user
```
## **Install GSM Parts**
In addition to the LTE components we have already discussed, we will also be using two GSM components in our system model: OsmoMSC and OsmoHLR.

OsmoMSC is a mobile switching center (MSC) component for GSM networks that provides support for voice and SMS services. OsmoHLR is a home location register (HLR) component for GSM networks that provides subscriber information and authentication services.

To install OsmoMSC and OsmoHLR, you can follow the instructions provided next:
### Install Libosmocore
```code
~/repos$ sudo sudo apt-get install build-essential libtool libtalloc-dev libsctp-dev shtool autoconf automake git-core pkg-config make gcc gnutls-dev python-minimal libusb-1.0.0-dev libmnl-dev libpcsclite-dev
```

```
~/repos$ git clone https://gitea.osmocom.org/osmocom/libosmocore.git
~/repos$ cd libosmocore/
~/repos/libosmocore$ autoreconf -i
~/repos/libosmocore$ ./configure
~/repos/libosmocore$ make
~/repos/libosmocore$ sudo make install
~/repos/libosmocore$ sudo ldconfig -i
~/repos/libosmocore$ cd ..  
```

### Install Libosmo-abis
```code
~/repos$ sudo apt-get install build-essential libtool libortp-dev dahdi-source libsctp-dev shtool autoconf automake git-core pkg-config make gcc
```

```
~/repos$ git clone https://gitea.osmocom.org/osmocom/libosmo-abis.git
~/repos$ cd libosmo-abis/
~/repos/libosmo-abis$ autoreconf -i
~/repos/libosmo-abis$ ./configure
~/repos/libosmo-abis$ make
~/repos/libosmo-abis$ sudo make install
~/repos/libosmo-abis$ sudo ldconfig -i
~/repos/libosmo-abis$ cd ..  
```

### Install Libosmo-netif

```
~/repos$ git clone https://github.com/osmocom/libosmo-netif.git
~/repos$ cd libosmo-netif/
~/repos/libosmo-netif$ autoreconf -i
~/repos/libosmo-netif$ ./configure
~/repos/libosmo-netif$ make
~/repos/libosmo-netif$ sudo make install
~/repos/libosmo-netif$ sudo ldconfig -i
~/repos/libosmo-netif$ cd ..  
```

### Install Libosmo-sccp

```
~/repos$ git clone https://github.com/osmocom/libosmo-sccp.git
~/repos$ cd libosmo-sccp/
~/repos/libosmo-sccp$ autoreconf -i
~/repos/libosmo-sccp$ ./configure
~/repos/libosmo-sccp$ make
~/repos/libosmo-sccp$ sudo make install
~/repos/libosmo-sccp$ sudo ldconfig -i
~/repos/libosmo-sccp$ cd ..  
```

### Install OsmoHLR

```
~/repos$ git clone https://github.com/osmocom/osmo-hlr.git
~/repos$ cd osmo-hlr/
~/repos/osmo-hlr$ autoreconf -i
~/repos/osmo-hlr$ ./configure
~/repos/osmo-hlr$ make
~/repos/osmo-hlr$ sudo make install
~/repos/osmo-hlr$ sudo ldconfig -i
~/repos/osmo-hlr$ cd ..  
```

### Install libsmpp34
```
~/repos$ git clone https://github.com/osmocom/libsmpp34.git
~/repos$ cd libsmpp34/
~/repos/libsmpp34$ autoreconf -i
~/repos/libsmpp34$ ./configure
~/repos/libsmpp34$ make
~/repos/libsmpp34$ sudo make install
~/repos/libsmpp34$ sudo ldconfig -i
~/repos/libsmpp34$ cd ..  
```

### Install Asn1c
```
~/repos$ git clone https://github.com/osmocom/libasn1c.git
~/repos$ cd libasn1c/
~/repos/libasn1c$ autoreconf -i
~/repos/libasn1c$ ./configure
~/repos/libasn1c$ make
~/repos/libasn1c$ sudo make install
~/repos/libasn1c$ sudo ldconfig -i
~/repos/libasn1c$ cd ..  
```

### Install OsmoMSC
```
~/repos$ git clone https://gitea.osmocom.org/cellular-infrastructure/osmo-msc
~/repos$ cd osmo-msc/
~/repos/osmo-msc$ autoreconf -i
~/repos/osmo-msc$ ./configure --enable-smpp
~/repos/osmo-msc$ make
~/repos/osmo-msc$ sudo make install
~/repos/osmo-msc$ sudo ldconfig -i
~/repos/osmo-msc$ cd ..  
```
## **Install open5gs**
open5gs is an open-source 5G core network implementation that provides support for a variety of 5G features, including 5G core network services, network slicing, and QoS management. We will be using open5gs to provide the core network component of our system model.

To install open5gs, you can follow the instructions provided bellow:
### Getting MongoDB
```code
~/repos$ sudo apt-get install gnupg
~/repos$ curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
   --dearmor
~/repos$ echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
~/repos$ sudo apt-get update
~/repos$ sudo apt-get install -y mongodb-org
~/repos$ sudo apt install -y mongodb-org
~/repos$ sudo systemctl start mongod (if '/usr/bin/mongod' is not running)
~/repos$ sudo systemctl enable mongod (ensure to automatically start it on system boot)
```
### Setting up TUN device (not persistent after rebooting)
```code 
~/repos$ sudo ip tuntap add name ogstun mode tun
~/repos$ sudo ip addr add 10.45.0.1/16 dev ogstun
~/repos$ sudo ip addr add 2001:db8:cafe::1/48 dev ogstun
~/repos$ sudo ip link set ogstun up
```

### Building Open5GS
```code
~/repos$ sudo apt install python3-pip python3-setuptools python3-wheel ninja-build build-essential flex bison git cmake libsctp-dev libgnutls28-dev libgcrypt-dev libssl-dev libidn11-dev libmongoc-dev libbson-dev libyaml-dev libnghttp2-dev libmicrohttpd-dev libcurl4-gnutls-dev libnghttp2-dev libtins-dev libtalloc-dev meson
```

```code
~/repos$ git clone https://github.com/open5gs/open5gs
~/repos$ cd open5gs
~/repos/open5gs$ meson build --prefix=`pwd`/install
~/repos/open5gs$ ninja -C build
~/repos/open5gs$ ./build/tests/attach/attach ## EPC Only
~/repos/open5gs$ ./build/tests/registration/registration ## 5G Core Only
~/repos/open5gs$ cd build
~/repos/open5gs/build$ meson test -v
~/repos/open5gs/build$ ninja install
~/repos/open5gs/build cd ~/repos
```


# Configuring the Software Components
To ensure that the system model works properly, it is important to configure the different software components correctly. Some components, such as the MME, OsmoMSC, and srsENB, are more critical than others and require extra attention during the configuration process.
## OsmoMSC
The OsmoMSC, or Open Source Mobile Switching Center, is responsible for the management of voice and SMS services in the system model. To configure the OsmoMSC, you will need to specify various parameters such as the MSC number, HLR address, and SMSC address. These parameters can be configured using the ```/usr/local/etc/osmocom/osmo-msc.cfg``` file provided by the OsmoMSC project.

This is a sample test configuration.
```code
!
! OsmoMSC configuration saved from vty
!
line vty
 no login
!
network
 network country code 1
 mobile network code 1
 short name OsmoMSC
 long name OsmoMSC
 encryption a5 0
 rrlp mode none
 mm info 1
 mgw 0
  remote-ip 127.0.0.1
  remote-port 2427
  local-port 2728

sgs
 local-port 29118
 local-ip 0.0.0.0
 vlr-name vlr.msc001.mnc001.mcc001.3gppnetwork.org
smpp
 local-tcp-ip 127.0.0.25 2755
 system-id hello
 policy accept-all
 no smpp-first
 esme hi
  password 123
msc
 assign-tmsi
 auth-tuple-max-reuse-count 3
 auth-tuple-reuse-on-error 1
```

## MME
The MME, or Mobility Management Entity, is a key component of the 4G core network that handles the management of user mobility and authentication. To configure the MME properly, you will need to specify various parameters such as the PLMN ID, TAI list, and security settings. These parameters can be configured using the ```~/repos/open5gs/install/etc/open5gs/mme.conf``` file provided by the Open5GS project.

This is a sample test configuration.

```code
logger:
    file: ~/repos/open5gs/install/var/log/open5gs/mme.log


mme:
    freeDiameter: ~/repos/open5gs/install/etc/freeDiameter/mme.conf
    s1ap:
      - addr: 127.0.0.2
    gtpc:
      - addr: 127.0.0.2
    metrics:
      - addr: 127.0.0.2
        port: 9090
    sgsap:
      addr: 127.0.0.1
      map:
        tai:
          plmn_id:
            mcc: 001
            mnc: 01
          tac: 1
        lai:
          plmn_id:
            mcc: 001
            mnc: 01
          lac: 1
    gummei:
      plmn_id:
        mcc: 001
        mnc: 01
      mme_gid: 2
      mme_code: 1
    tai:
      plmn_id:
        mcc: 001
        mnc: 01
      tac: 1
    security:
        integrity_order : [ EIA2, EIA1, EIA0 ]
        ciphering_order : [ EEA0, EEA1, EEA2 ]
    network_name:
        full: Open5GS
    mme_name: open5gs-mme0

sgwc:
    gtpc:
      - addr: 127.0.0.3

smf:
    gtpc:
      - addr: 
        - 127.0.0.4
        - ::1


parameter:

usrsctp:


time:
```

## srsENB
The srsENB, or software-defined Radio Access Network eNodeB, is responsible for handling the radio communications between the user devices and the 4G core network. To configure the srsENB, you will need to specify various parameters such as the frequency band, cell ID, and MCC/MNC. These parameters can be configured using the ```/home/gcatcher/.config/srsran/enb.conf``` file provided by the srsENB project.

### Other Components
All the necessary configuration files are provided in the "configs" folder of this repository. To properly run the system, it's essential to correctly configure the MME, OsmoMSC, and srsENB components. Make sure to carefully follow the instructions and modify the configuration files according to your specific setup before running the software.

# How to use?
1. Create an applet: First, you need to create an applet that you want to install on the phone. An applet is a small software program that performs a specific task. For example, you can create an applet that displays a message when the phone is turned on.
2. Convert the applet to a binary file: Once you have created the applet, you need to convert it to a binary file. A binary file is a file that contains executable code that can be run on the phone.
3. Send the binary file via OTA SMS: You can send the binary file to the phone via OTA SMS. OTA SMS stands for Over-The-Air SMS, which is a method of sending SMS messages that contain executable code. The phone will receive the OTA SMS and automatically install the applet.
4. Verify the applet installation: Once the applet has been installed, you can verify that it is working correctly by running it on the phone.
5. Delete the applet: To delete the applet from the phone, you can send another OTA SMS message that contains a command to delete the applet. The phone will receive the OTA SMS and automatically delete the applet.

# 1. Create an Applet and convert it to an APDU
## Shadytel SIM Tools
Shadytel SIM ([Main Project](https://gitea.osmocom.org/sim-card/sim-tools/)) tools are a set of open-source software components that provide support for SIM card emulation and management. The Shadytel SIM Tools project also includes a set of tools for creating Application Protocol Data Units (APDU) that can be used to write SIM Toolkit Applets. SIM Toolkit Applets are small software applications that run on the SIM card and provide additional functionality beyond the standard GSM features.

To download a sample applet and convert it to APDU using Shadytel, follow these steps:

1. Clone the sim-tools repository:
```code
~/repos$ git clone https://github.com/herlesupreeth/sim-tools.git
```
2. Clone the "hello-stk" sample applet and then Build the applet:
```code
~/repos$ git clone https://gitea.osmocom.org/sim-card/hello-stk
~/repos$ cd hello-stk/hello-stk/
~/repos/hello-stk/hello-stk$ make
~/repos/hello-stk/hello-stk$ cd ~/repos/sim-tools/shadysim
```
Run the Shadytel command to convert the applet to APDU:
```code
~/repos/sim-tools/shadysim$ python3 shadysim_isim.py --pcsc -l ~/repos/hello-stk/hello-stk/build/javacard/org/toorcamp/HelloSTK/javacard/HelloSTK.cap -i ~/repos/hello-stk/hello-stk/build/javacard/org/toorcamp/HelloSTK/javacard/HelloSTK.cap \
          --enable-sim-toolkit --module-aid d07002ca44900101 \
          --instance-aid d07002CA44900101 \
          --nonvolatile-memory-required 0100 \ 
          --volatile-memory-for-install 0100 \
          --max-menu-entry-text 15 \
          --max-menu-entries 05 --kic KIC1 \
          --kid KID1 \
          --smpp
```
After converting the sample applet to an APDU, we can send it to the phone using a SMPP client. We can send several APDUs to perform different operations on the phone, such as sending SMS or making calls. To do this, we need to have access to a SMPP server that can handle our requests. In our case, we are using OsmoMSC as the SMPP server. We can send the APDUs to the SIM card by connecting to the SMPP server using a SMPP client. The OsmoMSC will then forward the SMPP messages over the SGS interface to the SRS eNodeB, which will in turn send the SMS messages to the SIM card.

To send an SMS message using an SMPP client, the client first establishes a connection with the SMPP server. This is typically done using the bind operation, which authenticates the client with the server and establishes a session. Once the session is established, the client can send SMS messages to the SMPP server using the submit_sm command.

In the case of our system model and GitHub page, we can use an SMPP client to send APDUs to OsmoMSC, which acts as the SMPP server. The APDUs can be sent as SMS messages using the SMPP protocol, and OsmoMSC will then forward the APDUs to the appropriate SIM card.

The SMPP client code can be found in the smpp directory provided for our system model. The code is written in Python and uses the smpp library to establish a connection with OsmoMSC. Once the connection is established, the client can send APDUs to OsmoMSC using the submit_sm command.

The shadytel command (mentioned above) gives us several APDUs, which are then saved in a list variable named parts. 
```
~/repos/sim-tools/shadysim$ cd ~
~$ mkdir scripts
~$ cd scripts
~$ nano OTA.py    # save the file (This is a commnet)
#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
import logging
import sys

import smpplib.gsm
import smpplib.client
import smpplib.consts

logging.basicConfig(level = logging.DEBUG,
	format = "%(levelname)s %(filename)s:%(lineno)d %(message)s")

client = smpplib.client.Client('127.0.0.25', 2755)

# Print when obtain message_id
client.set_message_sent_handler(
	lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))
client.set_message_received_handler(
	lambda pdu: sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id)))

client.connect()
client.bind_transceiver(system_id='hi', password='123')

def send_normal(string='', dest='1234', source='1234'):
	parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(string)
	#part = b"".join(parts)
	try:
		string.encode("ascii")
		coding = encoding_flag
	except:
		coding = smpplib.consts.SMPP_ENCODING_ISO10646
	logging.info('Sending SMS "%s" to %s' % (string, dest))
	for part in parts:
		pdu = client.send_message(
			msg_type=smpplib.consts.SMPP_MSGTYPE_USERACK,
			source_addr_ton=smpplib.consts.SMPP_TON_ALNUM,
			source_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
			source_addr=source,
			dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
			dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
			destination_addr=dest,
			short_message=part,
			data_coding=coding,
			esm_class=msg_type_flag,
			#esm_class=smpplib.consts.SMPP_MSGMODE_FORWARD,
			registered_delivery=True,
		)
		#print(pdu.generate())
	logging.debug(pdu.sequence)


def send_ota(dest='1234', source='1234'):
	parts = [
		"027000003815060115150000003195dbcde566d446530344668ac12e0297644e40c37f9c304458542bbe49d311ca134012c29b073b70c17974d4fbe00e",
		"0270000068150601151500000093f53ae199da31cdee0c54b4b2f752a0541f52e60abe1cdce2b80e4be4d0dfeb6782bf434a075e0f49d96405891e8dac0bd341c42e9fd79b3c643164da1bfb1b1c7f5fd6c0a432e42599a1ac2667ae440b51e0e72a5ac766443ee3021ea3c71e",
		"027000006815060115150000000ac6e4282d7a1c15efcbbb9b67a0719248b2f9f00c5b7bf1f77ef28516f9bdb6783d00799d56622a92206c11db865b786185fe2f3bd9a51184207b9f7e29c19ff453a371b0fdba6b7313c0bac103dd09cd5614abe427158307ef3c9a0198a1a9",
		"02700000681506011515000000cdaf748da20a6379092226fe988f0bcfc0a1090dd44dd83d2dec74be6d98aff0a7ada1cfe87c8105eecf17cd6f6b806b9f74e82279e650628a325c3dea58c63c167fc4792183b6b1e0ae4031a5fb03544ab014afd4cb78140fdc1024cbfc917f",
	    "0270000068150601151500000014f40e210b02d9657ac3782c44f9a8d9d2b7eae662db03b0a175527d0dc4828bfa9c3ebe0bd8fc7fce7d9cf33c2f2eb5807d942d17ab9fe76f523df8834fc2ef147de2a1d9e96b39267a2125c24df89a0f0ec1fe539e09dcf1c4400e51043dc3",
	    "027000006815060115150000000c7e602ab93fce7d80191ddb7dd9ee2e985c92ef1e533cc6d64d4fde4e6e5733d233eddcb67d24bca6f62ccd8258812576818745be41262e4a6848b1ec137467e8962d1d6433731552ce3e81beec4eb572fcdcb5acd8e805edcdd783f30ed00e",
	    "02700000581506011515000000b1526b32cf5b52c20a2c9ee0d4dbc2c93c43d1c760369963af265f9cbac1f813fe7156be887d8cd69eee2d7a2c900f9ecf777d7ee8e7162c3134eefb6dae7f7e9aa058e3eb51985aeee463142ceb16d4",
	    "027000006015060115150000006b23de2bddfefbc723085bee46081c93977d5fc9e55d1b568e203f1ce10c8c228976201c7f3c5be313dff41210aafc591f13ccd2a2913384ac55e85b9cc77d1e7066bda84bcb9dc8166013f6ab09aed9f882ef7cd2e73436"
	]   
	# parts = [
	# 	"02700000301506011515000000d7d5afccd1161ebf2c64850167628c59b8684fd115542c39aac5a4fa8b1a53f0dc2816b48bdffdfb"
	# ]
	# logging.info('Sending OTA PDU to %s' % (dest))

	for part in parts:
		pdu = client.send_message(
			# source_addr_ton=smpplib.consts.SMPP_TON_INTL,
			# source_addr='0',
			dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
			destination_addr='12345678900',
			short_message=bytes.fromhex(part),
			data_coding=246,
			esm_class=64,
			registered_delivery=True,
		)
		print(pdu.sequence)


if __name__ == "__main__":
	# message = sys.argv[1]
	# send_normal(string=message)
	send_ota()

```
To delete the applet same process goes on with a little difference:
```code
~/repos/sim-tools/shadysim$ python3 shadysim_isim.py --pcsc -d d07002CA449001 \
          --kic KIC1 \
          --kid KID1 \
          --smpp
```
This command (mentioned above) gives us several APDUs, which are then saved in a list variable named parts. As mentioned in the python code above, there are two list variables named parts, one for deleting and one for installing the applet. You can commnet one of them as you want to install or delete the applet.
# 2. Running open5gs Components
Better to use something like Tmux.
```code
# Terminal 1
~$ ~/repos/open5gs/install/bin/open5gs-mmed
```
```code
# Terminal 2
~$ ~/repos/open5gs/install/bin/open5gs-hssd
```
```code
# Terminal 3
~$ ~/repos/open5gs/install/bin/open5gs-pcrfd
```
```code
# Terminal 4
~$ ~/repos/open5gs/install/bin/open5gs-sgwcd
```
```code
# Terminal 5
~$ ~/repos/open5gs/install/bin/open5gs-sgwud
```
```code
# Terminal 6
~$ ~/repos/open5gs/install/bin/open5gs-smfd
```
```code
# Terminal 7
~$ ~/repos/open5gs/install/bin/open5gs-upfd
```

## 2. Running GSM Components
```code
# Terminal 8
~$ sudo osmo-msc -c /usr/local/etc/osmocom/osmo-msc.cfg
```
```code
# Terminal 9
~$ sudo osmo-hss -c /usr/local/etc/osmocom/osmo-hss.cfg
```

# 3. Register Subscriber Information in HSS (open5gs) database
You can refer to [Open5gs](https://open5gs.org/open5gs/docs/guide/02-building-open5gs-from-sources/) for more information

# 4. Register Subscriber Information in HLR (osmocom) database
Make sure osmo-hlr is running.
```code 
~$ sudo telnet 127.0.0.1 4258
OsmoHLR> enable
OsmoHLR# subscriber imsi THEIMSI create
# Check as bellow (This is a comment)
OsmoHLR# show subscribers all
ID     MSISDN        IMSI              IMEI              NAM
-----  ------------  ----------------  ----------------  -----
1      none          123456789          -------------    CSPS
# Update MSISDN so you can send SMS and OTA (This is a commnet)
OsmoHLR# subscriber imsi THEIMSI update msisdn THEMSISDN
OsmoHLR# show subscribers all
ID     MSISDN        IMSI              IMEI              NAM
-----  ------------  ----------------  ----------------  -----
1      1234          123456789          -------------    CSPS  
 Subscribers Shown: 1
```
# 5. Run the following Script to install/delete the applet
```code
$ python3 smpp.py
```
