int convert(long long bin);

int main() {
    long long bin;
    return 0;
}
/*
La siguiente funcion convierte un numero
*/
int convert(long long bin) {
    int oct = x = 0, dec = 0, i = 0;
    float var = -1.2345;

    // converting binary to decimal
    while (bin > 0) {
        dec += (bin % 10) * pow(2, i);
        ++i;
        bin /= 10;
    }
    i = 1;

    // converting to decimal to octal
    while (dec != 0) {
        oct += (dec % 8) * i;
        dec /= 8;
        i *= 10;
    }
    return oct;
}