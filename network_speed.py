import speedtest as st

def Speed_Test():
    test = st.Speedtest()

    ds = test.download()
    ds = round(ds / 10**6, 2)  # Se convertesc bitii in megabiti
    print("Viteza de descarcare: ", ds, "Mbps")

    us = test.upload()
    us = round(us / 10**6, 2)
    print("Viteza de incarcare: ", us, "Mbps")

    ping = test.results.ping
    print("Ping: ", ping, "ms")

Speed_Test()

