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
