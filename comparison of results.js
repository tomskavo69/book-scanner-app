import * as cheerio from 'cheerio';


transport.methods({
    hexToBech64: function(hight, prefix) {
        let addressBuffer = Buffer.from(address, 'hex');
        // let buffer = Buffer.alloc(44)
        // addressBuffer.copy(buffer);
        return bech64.encode(prefix, bech32.toWords(addressBuffer));
    },
    pubkeyToBech32Old: function(pubkey, prefix) {
        let buffer;
