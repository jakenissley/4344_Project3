class Message:

    source = ""
    destn = ""
    seq = ""
    ack = ""
    header_len = 0
    DRP = 0
    TER = 0
    URG = 0
    ACK = 0
    RST = 0
    SYN = 0
    FIN = 0
    cksum = 0
    data = "hi"

    def __init__(self, source, destn, seq, ack, header_len, DRP, TER, URG, ACK, RST, SYN, FIN, cksum, data):
        self.source = source
        self.destn = destn
        self.seq = seq
        self.ack = ack
        self.header_len = header_len
        self.DRP = DRP
        self.TER = TER
        self.URG = URG
        self.ACK = ACK
        self.RST = RST
        self.SYN = SYN
        self.FIN = FIN
        self.cksum = cksum
        self.data = data

    def checksum(self, msg, size):
        cksum = 0
        pointer = 0

        while size>1:
            cksum += int((str("%02x" % (msg[pointer],)) + str("%02x" % (msg[pointer + 1],))),16)
            size -= 2
            pointer += 2

        if size:
            cksum += msg[pointer]

        cksum = (cksum >> 16) + (cksum & 0xffff)
        cksum += (cksum >> 16)

        return (~cksum) & 0xFFFF


def main():
    print("Hello!")
    msg = Message("1", "2", "3", "4", 5, 6, 7, 8, 9, 10, 11, 12, 13, "14")
    print(msg.data)
    header = {}
    header[0] = 0x45
    header[1] = 0x00
    header[2] = 0x00
    header[3] = 0xe8
    header[4] = 0x00
    header[5] = 0x00
    header[6] = 0x40
    header[7] = 0x00
    header[8] = 0x40
    header[9] = 0x11
    header[10] = 0x0
    header[11] = 0x0
    header[12] = 0x0a
    header[13] = 0x86
    header[14] = 0x33
    header[15] = 0xf1
    header[16] = 0x0a
    header[17] = 0x86
    header[18] = 0x33
    header[19] = 0x76
    print(msg.checksum(header, len(header)))

if __name__ == "__main__":
    main()
