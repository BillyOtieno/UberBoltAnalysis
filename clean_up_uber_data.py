import re
import pandas as pd


def main():
    pd.read_excel()
    total_price = re.compile()
    string_to_clean = """
        Total: KES 430 
        Fri, Nov 30, 2018    
        
          
          
        Thanks for riding, Billy 
        We hope you enjoyed your ride this evening. 
           
        Total KES 430 
          
        Trip fare KES 430 
          
        Subtotal KES 430 
          
        Amount Charged   
        Paid in cash 
        |
        Switch 
        <https://email.uber.com/wf/click?upn=ITf-2BUi9bO5sUhPgUfzyAxiAlszZJrA2yIT7-2FMFM5bgsbN8U-2FhX3QvurlDc-2BhZ8CKBLruCMKTq7WJBn82Ool-2B7dauShI-2BG7ZVVpKW7eci3eA-3D_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnIv9CVwvs-2B44uAwARddnhm2wmS-2B1zsGzYS1XDEy4r9F5l8XJRFrLdk4GdYALiHSvDDXNPRto-2BuwfN-2FuFlG0tNrSUxmfXIHoEk0HxwqhqWEA0rAHZoPhNXZyGcq8dEiVbBS50cGwGopcwz-2BiELVA8CEs-3D> KES 430 
        
        Visit the trip page 
        <https://email.uber.com/wf/click?upn=E5Fht-2Bzc2SrMWnjw-2Brx3-2BCge-2BTDCYy8uto5SQzU7fOfKAepWbBX7WOdAkWZ7tenJbk8sTshiLeKmYQj4SDMU-2FB29Y1wd8ESsdITlGy0lWWw-3D_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnFMqkVb4b-2FIyOx9i8wq8Fx-2BHfeecaIFbr-2B2u898F8Vee56tHrLpP34Z7uneVLmK6B7DWRhiQLw5QjFVrz89NHT7hG37rOmY-2F-2BgK7aoZT-2FU0vm1e8-2B-2FMOJZbVmatdGPlj5T7vkd7hrT6qUxk1j-2BFKGfs-3D> 
        for more information, including invoices (where available) 
        Download PDF 
        <https://email.uber.com/wf/click?upn=RPcWxkTQoG6P9NvXwlv2wYxWh93fPYNEuoSsYWZV2yO81vUt3l9K54NalrT9bnDz3cHj6vKoTqc2HetSTpLf6IPXv7FRvJuKEahvybIv6LbF6fG0XFAJ-2FXjvvUW3VF5UpazHCSFCKk71h-2FCkq-2FpMrAiKB4akTn2bMGADRzZ-2FP6o7w9aTLl1IUsw0lp7kxYqSWzLh2qrHxZnPeQFCKpz4qxQ87MntLGUTddAJ0nflZ15xG6Q6TMKIynhdzENaN-2FpjCLmR8TaMQxdOHmFS58qma5DgttynGJaU94YOCOmKw5LMTAVSsQmMQLKlgMdJHNm4Ucbdke6bjn1jQ1zEPJNlKX4UDKGP7PzKwpkpNWEXvzVEotV61r5L4AWYo8q9AWHz-2FPMCNsVK11atuGUJxsDtg05DEmdaNh0vmrry9WGxE-2Bes-2BcCV2fo2VX6uGNk0oxzqY2XjOlDIUgd7SR6tSj1tfxIsnpxxasfUmCWYlnKgTZOHHQmO4976OePeEIFdv3xEguFMQ8e0g04XOwrv0EnUcq1DQRI1lbNzt6aHnrx-2FbZTni4X4ZDurIJwRWUwrusLk-2BCq6kHu0zkx0yuLo12q3szH49AdQhkCpW0pE4Vn2rkxRlBjp0XYfIQ6Fk1Jf4gaElGk33w5-2FEDxWCM1mWSEUAqrDvP8bOZ5cT286TmfJlx3cSsz1IYpmsjUmcc5LJOU8SfNlpC37rfzPfmSCDpCo1A-3D-3D_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnEHuGPqqxitVpm8JO-2F174U7VHWvq8H-2B1pGLr5qQHB9n7uMm6AfRbIoN6qXy0S5YFeJoQFDiuS6kKeEQ4bPVcmuPoYqw9odkXcbfVZtoXD79Mze1CFUW5K8gEr-2B7LO4hbno-2BXde8-2BVM-2FiOWDjQ8UJX0U-3D>
        Download link expires on 30/12/2018 
        xid37468294-735c-4deb-ac5e-6c97cc6c3cbc 
        pGvlI2ANUbXFfyEOgxta1RMV082993 
         
         
        You rode with Burton 
        4.72 Rating 
         
        Top driver compliment 
        ""Excellent Service"" 
        How was your trip? 
        
        Rate now 
        <https://email.uber.com/wf/click?upn=E5Fht-2Bzc2SrMWnjw-2Brx3-2BCge-2BTDCYy8uto5SQzU7fOfKAepWbBX7WOdAkWZ7tenJbk8sTshiLeKmYQj4SDMU-2FB29Y1wd8ESsdITlGy0lWWw-3D_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnCLOcp2HHZwhFplcmbCmiMwyNE1-2BE7CanuKe5RDvmJXNQjr-2BtpSrQ5VxYpmjSTj9oNmcAPYi5F-2F62WsQRcPWs-2BB9rmjJhMFFbIi1w7X1FkEHgpJVY7kpm4PHMpsj4PC30MaAjdfLxs6jy9nhn1i9nC4-3D>
        Rate now 
        <https://email.uber.com/wf/click?upn=xH5uxoMqK-2FRRJL3c3WgT-2FNGgq-2FxihEsxp555tySQvIuBa-2Fs7-2F7RFpL10D5usjTvD_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnFXG0mfCy-2BU8ubcOwsFLu-2BBOBDZbWDSKvsrZD7kjIb9Az3EvqkSurz9w-2FFQK9SAhCxwTdnN-2FTDifiSxyCW8FvaMmBc2JU2aPPFBP0XDgTjoXQoVE4uo163hEc0uoNhRpiZp9KWlRjsw-2BFSftvHiX-2FjE-3D>
        License Plate: KCR 760B 
         
        
        Chapchap 
        5.83 km | 20 min(s) 
        18:09 
        City Hall Way, Nairobi, Kenya 
        18:30 
        Egeyo, Nairobi, Kenya 
        
        Invite your friends and family. 
        Get a free trip worth up to KES 250 when you refer a friend to try Uber. Share 
        code: billyo925ue
        Report lost item ❯ 
        <https://email.uber.com/wf/click?upn=ITf-2BUi9bO5sUhPgUfzyAxge7rrmc1TB7MBPB0UVnv5WCgF8LXIrzArIFbD9VI0oCzeEZ-2BotxfMsld31I7yAsyBw6-2FN-2F5-2F0mi2b7tjaXiF-2FQ-3D_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnOw-2B0meiyIfPiws91w80aeT-2BtwdGMxnvC5KsUYp4vGPv73tPGKxIX6qCa9o-2FpbPh5i0U-2FmmDPU2-2F7b0OvwPRtxXMnCJ4-2FMoLV4sRIFtm3VEGubmnG-2BN1Ji2Q8iF5a-2FKXeXLgxpcOiFzFJVNwuviz0Pw-3D> 
         
        
        contact support ❯ <help.uber.com/riders>
        contact support ❯ 
        <https://email.uber.com/wf/click?upn=ivypI-2BHDlrQ9K35dDx4zB8KS6X-2F0d-2FtVObre3fnwNqlHonaXHMIn3l-2B8Qfkdx2Ca_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnA9P4NTDjm-2FSSlKOSPXQxUku5f-2FOjLlJMtXFL-2Fsj3uYP2Rw0itQcgJAvt-2BdoQqRcY11Zdd3iV46rlURekKhWZOsOb4glzflskcZL9ZYB4Jfhl-2B3grkRt-2B-2BLYNgQiDllermQvZXxKF9YyrbcwVSEquXg-3D>
         
        My trips ❯ 
        <https://email.uber.com/wf/click?upn=E5Fht-2Bzc2SrMWnjw-2Brx3-2BCge-2BTDCYy8uto5SQzU7fOeY8Whb9IQreODC4SHBE5F-2F_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnLXjQ0Am4OoWmLUGWN7iipYv6n1vRyvTe6WgOcSuS-2F3wsy5OwpLfysXaW3ffO0KEaDcGD3DHRu1xXr-2B-2Fbune55M5WcXQDZBu3m3Abrl5WMcwsfOIcQAaDMFpV-2BLPWb4kjaK0-2BvIWDBaEf4jNRxlyDB4-3D> 
         
         
         
        FAQ 
        <https://email.uber.com/wf/click?upn=ITf-2BUi9bO5sUhPgUfzyAxj5iFqf-2FESRS16p6bw9B-2BMWQqZiB-2BxjwRgeYbkjgMWvF_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnHJ6q9toni7bDfjy0easI-2BKPOwZK0RTcK5mh6GY9nqfkSoTlWJKNZHK79RDIrXBguoGwnavjnYKG3chrBBbJoMlL7SqRcJ5aU2vGhNLovISOq-2BKXTAiaVHAZEx1VlkjwihBuOuR9uLe63oxekv-2BWTrY-3D>
        Forgotten password 
        <https://email.uber.com/wf/click?upn=ITf-2BUi9bO5sUhPgUfzyAxlPMkOdjjGMakTnjAIL7ePbKucTAwAxSOg7sPFFwzO5-2B-2BglOH2JuMg5JUK-2FYad4pICydKL0iBSnjTpe51IrGTwRLEmCubJfdjPReIlrwPUAbm-2BRa8IlcPD1k4P-2FiqEPsnM-2BEfr2iw7XxRtBPojNVhf25iKPLWtcMAKB4WYVSs4LF43eBnL-2BnKCTd1iwRDwZ-2FHg-3D-3D_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnKoZt5px9PQgSa0q9qZdvhGApwolmOuhUe-2Bxx91awKiHVcl69yTDDWoMlJmKC0VXhlG3wVnXz0gUHr2dxK7bf76XGaZePhSuERXBxoqTXLULIF-2FTgRimQkqEge02SzFcOIc22rtFv-2BHN5dpjMN01cK4-3D>
        Uber B.V.
        Mr. Treublaan 7
        1097 DP Amsterdam
        Privacy 
        <https://email.uber.com/wf/click?upn=Ac78kxLEU5x8sS8qIl5fKYosFxWyY-2FjhtDBZJR9cgRMpTXhOJzfGu1oYSzU-2FgYli_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnNqfFqwFQ5Y51bVYZLnc7VrQHrVEGy9p2zYGHMcnMZsZOCYbDa2B1wdI9Tx1VGRSd3sskVm4TTHH3fejudodMtGv2qFeckMc2ACE2UYAZkYMR69nwEvgOJfPP8gzuNUECTw4Dn6iY-2B4XCILqTu7DA0o-3D>
        Terms 
        <https://email.uber.com/wf/click?upn=Ac78kxLEU5x8sS8qIl5fKYosFxWyY-2FjhtDBZJR9cgRO3B5BmldvuwJiY27V6X-2BB-2B_Y28Qb2IHIMOD1N1Hrg92zuD6yk1CZzmLBupMvNF6WpCUw8sjqzRV1xsE8nZ7DRJlXIYz2Xxh-2F4LcYELPyTeAN4QlpZARzvp3m6OxQwFqP63XIHIlMzI4CvP-2BvCyWrpnUgb9oqb-2Fs3h9oZe2Mzpp6HVpfrhAsI8oL8i5JWgLWJvTKL5KJGAvmz7wNGJdO6MTIl-2BW-2FMeonJKC8-2FRTRSYC0y22LjwwoKFHLH-2FAbEibIhlZUmJ6KECiXM9vMcy3v87SrECw-2FVnsZ5xKPt4CCUK0dnGzjVKTyU6siDgjN1fcrXh1b7nKPZIgRPw2QV5KVR1B7mMQZhbp1iQdZsVGdgN6gQzIVZKtr6ADxePTzfn1ZQNmNv-2F4jO-2BDQNld8E8Gvm-2FTSiN33Yaz8kGg3loeCH37UsEMR-2Bfs-2B5psdMju-2BKPfZO14-3D>
         
        Fare does not include fees that may be charged by your bank. Please contact 
        your bank directly for inquiries.

    """

    print(string_to_clean)


if __name__=='__main__':
    main()

