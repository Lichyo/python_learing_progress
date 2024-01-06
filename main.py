import smtplib

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    result = connection.login('lichyo003@gmail.com', 'ufku seeg iraa vlir')
    connection.sendmail(
        from_addr='lichyo003@gmail.com',
        to_addrs='lichyo003@gmail.com',
        msg=f"Testing if I could send email from python".encode("utf-8")
    )
