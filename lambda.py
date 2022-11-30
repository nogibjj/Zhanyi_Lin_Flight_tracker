import pandas as pd
import numpy as np 
import connect_ec2
import flight_scrap
import upload
import os

parser = argparse.ArgumentParser()
parser.add_argument('outcity', help='the outbound city')
parser.add_argument('incity', help='the inbound city')
parser.add_argument('out_date', help='outbound date')
parser.add_argument('in_date', help='inbound date')
args = parser.parse_args()
outcity = args.outcity
incity = args.incity
out_date = args.out_date
in_date = args.in_date

expedia = Expedia()
toadd = expedia.search("RDU","ORD","12/07/2022",None)
df_master = pd.read_scv(zhanyil2_flight_pirce.download_file('master.csv', './master.csv'))
df_master.loc[df_master.shape[0],:] = toadd
df_master.to_csv("./master.csv")
upload.upload_file("./master.csv", zhanyil2_flight_pirce, "master.csv")
os.remove("./master.csv")