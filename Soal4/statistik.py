def rentang(data):
    return (min(data), max(data))


def ringkasan(data):
    return {
        "jumlah": len(data),
        "min": min(data),
        "maks": max(data),
        "rata": sum(data) / len(data)
    }


if __name__ == "__main__":
    data = [12.0, 15.0, 15.0]

    print("Rentang:", rentang(data))

    r = ringkasan(data)
    print("Ringkasan:", r)
    print("Rata-rata:", r["rata"])