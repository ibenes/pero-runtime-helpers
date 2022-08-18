#!/usr/bin/env python3

import argparse
import socket
import smtplib

from email.message import EmailMessage

def main(args):
    msg = EmailMessage()
    msg['Subject'] = f'{args.subject}'
    msg['From'] = f'{args.from_address}'
    msg['To'] = f'{args.to}'
    msg.set_content(f'{args.content}')

    print(msg)

    with smtplib.SMTP('kazi.fit.vutbr.cz') as s:
        s.send_message(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--to', required=True)
    parser.add_argument('-f', '--from', dest='from_address', default=f'pero@{socket.gethostname()}')
    parser.add_argument('-s', '--subject', required=True)
    parser.add_argument('-c', '--content', required=True)
    args = parser.parse_args()

    main(args)
