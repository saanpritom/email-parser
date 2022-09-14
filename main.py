# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



[('Delivered-To', 'mevrikdev@gmail.com'),
 ('Received', 'by 2002:a05:6638:5af:b0:342:8f9d:d1c6 with SMTP id b15csp1512646jar;\n        Mon, 8 Aug 2022 05:18:47 -0700 (PDT)'),
 ('X-Google-Smtp-Source', 'AA6agR7e+m0GCCZvYnW8zdRBp+32vXrFncUf6JcmGl15d6YyiWcp3v1be4wd0OoIouPzzudefuod'),
 ('X-Received', 'by 2002:a17:902:e892:b0:170:c2f:cb40 with SMTP id w18-20020a170902e89200b001700c2fcb40mr12901179plg.2.1659961127252;\n        Mon, 08 Aug 2022 05:18:47 -0700 (PDT)'),
 ('ARC-Seal', 'i=2; a=rsa-sha256; t=1659961127; cv=pass;\n        d=google.com; s=arc-20160816;\n        b=0ZlLYUbBJ8Ifr6gO65Sj0rFJSJwR//4jq8jVqu8lkDctbe216iBIzfQXW4IynjrLEP\n         foJVgE4SQNQ+MlnlvYhWneLllZdmhI2DcYmr4Ple4LM4eGDxm+ItbQ8+34yzXEpVyCB7\n         wQxvF1/ho3f/AHnXZ13LD3ugggDauV7L4WsYwWLs2SLHjdUkUu30UvQoBOF9E6KpkIy7\n         OACpcgH0Twy11OA8/pViUlJoOZOt/AOaDGHHSMo0VLpel4s4ZiW4H/qH/2udUYWaWSnW\n         VjqfGYAYKuAiWQxs2nTzHEHAsCWzYTeePWzCKsRElOSkWuroWf+lNgLkoI+FDlko18bV\n         yvIg=='),
 ('ARC-Message-Signature', 'i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;\n        h=mime-version:auto-submitted:in-reply-to:references:message-id:date\n         :thread-index:thread-topic:subject:to:from:dkim-signature;\n        bh=FR615SOaBPlvm8Zb7nywz7EE3KOXDh3cJMpkVT+1kqw=;\n        b=K+BLjDUHCNcLC6BHAGdLD6Tyd+5/MFDfc+giSlyYyO0LjwduS5w89co9SUZS4/HPZ2\n         5iViVoSg/Yh1h+Tu9yvtaIeHO0RwXqlAsiPU0JMBzjAwysd+YU9tQwpTV8Mw+Lj4wACF\n         3kqiHFEOYDJUZRrqo7yP7Obryk9fv0pMeUr51yCVLrix36CVwgPlvk4e4TqNGuI8xMvF\n         2Vh3TzoPf9D7q3xYFmdwj1VgHaOn0d4gnX+JagpfMEIkDlefTy9ANNZyIAYDplfTZIUe\n         fwuhOJpZH3uuQWUJnoGK7oTF5NTSbmBWIhFSQC/jdtCd2zaPnJPeXoFIcK7WILh/ukzg\n         jTXQ=='),
 ('ARC-Authentication-Results', 'i=2; mx.google.com;\n       dkim=pass header.i=@genexinfosysltd.onmicrosoft.com header.s=selector1-genexinfosysltd-onmicrosoft-com header.b=o99LZmR7;\n       arc=pass (i=1 dkim=pass dkdomain=genexinfosys.com dmarc=pass fromdomain=genexinfosys.com);\n       spf=pass (google.com: domain of postmaster@apc01-sg2-obe.outbound.protection.outlook.com designates 52.100.164.214 as permitted sender) smtp.helo=APC01-SG2-obe.outbound.protection.outlook.com'),
 ('Return-Path', '<>'),
 ('Received', 'from APC01-SG2-obe.outbound.protection.outlook.com (mail-sgaapc01hn2214.outbound.protection.outlook.com. [52.100.164.214])\n        by mx.google.com with ESMTPS id me2-20020a17090b17c200b001f21d415eacsi13087747pjb.185.2022.08.08.05.18.46\n        for <mevrikdev@gmail.com>\n        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);\n        Mon, 08 Aug 2022 05:18:47 -0700 (PDT)'),
 ('Received-SPF', 'pass (google.com: domain of postmaster@apc01-sg2-obe.outbound.protection.outlook.com designates 52.100.164.214 as permitted sender) client-ip=52.100.164.214;'),
 ('Authentication-Results', 'mx.google.com;\n       dkim=pass header.i=@genexinfosysltd.onmicrosoft.com header.s=selector1-genexinfosysltd-onmicrosoft-com header.b=o99LZmR7;\n       arc=pass (i=1 dkim=pass dkdomain=genexinfosys.com dmarc=pass fromdomain=genexinfosys.com);\n       spf=pass (google.com: domain of postmaster@apc01-sg2-obe.outbound.protection.outlook.com designates 52.100.164.214 as permitted sender) smtp.helo=APC01-SG2-obe.outbound.protection.outlook.com'),
 ('ARC-Seal', 'i=1; a=rsa-sha256; s=arcselector9901; d=microsoft.com; cv=none;\n b=Ro27S9l2Uc8xFKbgjtqVYO0GnPdURWrvWhofO9WLtX/1H+clG7GCLFtCNjdw4ZqzDyytypR6NS7qdracFL2/IZbb4+AYIRzWuSnOHM7NExEWlsgCgly3bJI43A4OYa9BB6or+ldP9rMStDY3Er/998FvQZzG3O/zRwq5ilL0skg9R1BNXTlEL5EX6OlAuBCvTtZlsWldRCtKycM2zHnzkpoX8NAX3/NTACVqrqj7bgPqgYiyByYnBoh6G71FRXVjBE7vPknzgHBWcBFJk8f9E54Qu9IokqKJSJu29/05mcojz5mQV6l6XzzcoOdRw+39R8G+CSmJdkTw1/PfQpIljw=='),
 ('ARC-Message-Signature', 'i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com;\n s=arcselector9901;\n h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1;\n bh=FR615SOaBPlvm8Zb7nywz7EE3KOXDh3cJMpkVT+1kqw=;\n b=MNEvar6jal8wV60oaixt1lpVBHPRkuJ9pafUAZ3oG0dFUm3m7RkMt1CKQPmVoUspgRP75AtrYM5vyafaT1KWpPMK9MlQsyTIIMvINL+BtXf83JdWx+Vw/WK1TsBzuQ1qP1cAEvDCbU9rOXWsG8RlS2LsjojQTmWD/kMqhc2TmHYXKV+GZAEzD5ooRJkhW4PbqA5NBfZXJ5SGFGRZNx0nxt0BryOevjghVtKBGwWw70jP3pvqQ1f0QgONumMfakXIbms0Ojzf8FtMqH9iaH8Z/XaTModG41sBZcm/ILfGG3YlfQPcTa6N9uTrgqHMaqnz8yIuV2XJhrC2WOO5bcIZTg=='),
 ('ARC-Authentication-Results', 'i=1; mx.microsoft.com 1; spf=none; dmarc=pass\n action=none header.from=genexinfosys.com; dkim=pass\n header.d=genexinfosys.com; arc=none'),
 ('DKIM-Signature', 'v=1; a=rsa-sha256; c=relaxed/relaxed;\n d=genexinfosysltd.onmicrosoft.com;\n s=selector1-genexinfosysltd-onmicrosoft-com;\n h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-SenderADCheck;\n bh=FR615SOaBPlvm8Zb7nywz7EE3KOXDh3cJMpkVT+1kqw=;\n b=o99LZmR7dSDZ4CmiiIS/ghfTykogqGjDt4Z65AjFzlCH2x/jN/PjUg+/S//Xf2bR9XHguqERoTLtIe0YmtWActWdojCWI2cb+M5FVaSUdHlyHoNQ5oAjJQVDvrFW9i5NNd4++g03z2MH/aoYTslgma9Ss8/0voHH5NDOCzKBNvE='),
 ('Received', 'from TYZPR04MB5233.apcprd04.prod.outlook.com (2603:1096:400:130::11)\n by KL1PR0401MB5517.apcprd04.prod.outlook.com (2603:1096:820:a8::14) with\n Microsoft SMTP Server (version=TLS1_2,\n cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.5504.16; Mon, 8 Aug\n 2022 12:18:44 +0000'),
 ('Received', 'from TYZPR04MB5233.apcprd04.prod.outlook.com ([::1]) by\n TYZPR04MB5233.apcprd04.prod.outlook.com ([fe80::e146:59c9:b5e4:4dcd%4]) with\n Microsoft SMTP Server id 15.20.5504.020; Mon, 8 Aug 2022 12:18:44 +0000'),
 ('From', 'Md.Reyad Hossain <reyad.hossain@genexinfosys.com>'),
 ('To', 'Grameenphone Customer Service From Grameenphone Customer Support\n\t<mevrikdev@gmail.com>'),
 ('Subject', 'Automatic reply: 122: 122 '),
 ('Thread-Topic', '122: 122 '),
 ('Thread-Index', 'AQHYpnFQizgE02bJVkq+V9juXmpZ5q2k9RcAgAAACCc='),
 ('Date', 'Mon, 8 Aug 2022 12:18:44 +0000'),
 ('Message-ID', '\n <1aa0663374034e118c7ebdda161f6ac2@TYZPR04MB5233.apcprd04.prod.outlook.com>'),
 ('References', '\n <TYZPR04MB5233451F1EFCCA84883BD2C5979D9@TYZPR04MB5233.apcprd04.prod.outlook.com>\n <165996111564.11.7033964519658319273@c386eafce177>'),
 ('In-Reply-To', '<165996111564.11.7033964519658319273@c386eafce177>'),
 ('X-MS-Has-Attach', ''),
 ('X-Auto-Response-Suppress', 'All'),
 ('X-MS-Exchange-Inbox-Rules-Loop', 'reyad.hossain@genexinfosys.com'),
 ('X-MS-TNEF-Correlator', ''),
 ('authentication-results', 'dkim=none (message not signed)\n header.d=none;dmarc=none action=none header.from=genexinfosys.com;'),
 ('x-ms-exchange-parent-message-id', '\n <165996111564.11.7033964519658319273@c386eafce177>'),
 ('auto-submitted', 'auto-generated'),
 ('x-ms-exchange-generated-message-source', 'Mailbox Rules Agent'),
 ('x-ms-publictraffictype', 'Email'),
 ('x-ms-office365-filtering-correlation-id', 'e72d4b2b-d72e-4aec-eea2-08da79382367'),
 ('x-ms-traffictypediagnostic', 'KL1PR0401MB5517:EE_'),
 ('x-ms-exchange-senderadcheck', '1'),
 ('x-ms-exchange-antispam-relay', '0'),
 ('x-microsoft-antispam', 'BCL:0;'),
 ('x-microsoft-antispam-message-info', '\n VqNCBOCmbomEliVhXW7XUw090higU+DFR4ti5kCq5qMzysN4T2MHrj5ds1+ztz00MKxCMAuInG/avkrvBpAhQ5X9ORn/WVnLPVVgoKjS5huvHLoSSgMI0WNG6FfcVMfcdlMWt1xKXd4zSAVzsKPYD/WYIpjrc+PwLk30aHb8o7NAeVSI0MLi8N8L8M88BCxBtpNTd8loLPuYXbgZFUncdwI40AF+2/GpNOf3k/aBTkdhrAtsvwWQ3q9AXyUM/tC7PJRBiv6iwSaNSJRZigHN+zeb+cH8eUFDdaFGhkYcU6aLpBMX3fRvcLOvPg/zkusW2H697M6FtZvuJuqk9rv9ydYVndFgwgx72lVenl0X0AZ3Uig91990+PKHG3oPcwXfR5V+2W+Gyo9eBC4kjhxyBbrQ6XEo4pSH9I+7vCmUIQdVSJhlWUQ+MVRASIdK/uF34XxAQuynhJl0QEn0qYXh1e8uHHVyb3yT28W8BR10ZLPz4asxUZgYg9w35B2RoRRtTZU5pE7UuBOQeXDZDRkYTTX31FfeU5n7Oj9r7vLgYUB7MEjHHkNKKJoVguLJvlRUMcYsMmTOuTtBghL9ToPjv8IjrixFFIUF4puUCrTSPc8DjSw3sQQrS+uVyo8m1gZYcofk2V/RxcvJC4BQChBjVI3wCCPdUWgZ8KOGdsGC8A7znxtl3opkVzlCTBNo1t9vnnWoMQ9LfB9TEcFtATICRk9w8p6Hd9nZKKiyemZMzSg='),
 ('x-forefront-antispam-report', '\n CIP:255.255.255.255;CTRY:;LANG:en;SCL:1;SRV:;IPV:NLI;SFV:NSPM;H:TYZPR04MB5233.apcprd04.prod.outlook.com;PTR:;CAT:NONE;SFS:(13230016)(50650200002)(376002)(366004)(39860400002)(396003)(346002)(136003)(122000001)(6506007)(83380400001)(4743002)(7696005)(24736004)(108616005)(42882007)(9686003)(88996005)(316002)(6916009)(71200400001)(41300700001)(498600001)(5660300002)(66556008)(66476007)(8676002)(66446008)(66946007)(78352004)(64756008)(8936002)(4744005)(2906002)(55016003)(111220200005)(80100003);DIR:OUT;SFP:1501;'),
 ('x-ms-exchange-antispam-messagedata-chunkcount', '1'),
 ('x-ms-exchange-antispam-messagedata-0', '\n r3fdTllKw1BOHQUYLmPVck3zbtpD0p1OwS2DJ84i7qo6Be2KTqtm9zSEaji6xrLkwzQqdtJ1F17v1n9kUrU/8xpUFUA4S+99RGybjGGfsd76lyIHkJocG5Udpkhq0Az6P5tpb2AJ9Zal+eFCNvRMg6Ov9rgte4DuMWsA82BhtAR6fgBTvIjNwh0knTqYRuuywzRn4zzyJtrpeH2DJMRSjPgYReptGKiVcneXf98hRgTmdw9zDpq17v2+65Q6TGD7vBMNwJAOSx7FFSxEvZOwWiewNd7VHU17ElpTIh4kDWJiGy79ryHKZ1+6HtwZdYmW'),
 ('Content-Type', 'multipart/alternative;\n\tboundary="_000_1aa0663374034e118c7ebdda161f6ac2TYZPR04MB5233apcprd04pr_"'),
 ('MIME-Version', '1.0'), ('X-OriginatorOrg', 'genexinfosys.com'),
 ('X-MS-Exchange-CrossTenant-AuthAs', 'Internal'),
 ('X-MS-Exchange-CrossTenant-AuthSource', 'TYZPR04MB5233.apcprd04.prod.outlook.com'),
 ('X-MS-Exchange-CrossTenant-Network-Message-Id', 'e72d4b2b-d72e-4aec-eea2-08da79382367'),
 ('X-MS-Exchange-CrossTenant-originalarrivaltime', '08 Aug 2022 12:18:44.5177\n (UTC)'),
 ('X-MS-Exchange-CrossTenant-fromentityheader', 'Hosted'),
 ('X-MS-Exchange-CrossTenant-id', '31d53faf-e76a-4f3f-8045-008c81c9777e'),
 ('X-MS-Exchange-Transport-CrossTenantHeadersStamped', 'KL1PR0401MB5517')]

"""obj.get_payload().get_payload(); For multipart first get_payload will be a list."""

