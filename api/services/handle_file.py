import csv


class HandleFile:
    @classmethod
    def handle_order_file(cls, file):
        line_count = 0
        validated_data = []
        for line in file:
            if line_count != 0:
                validated_data.append(
                    {
                        "order_id": int(line.decode("utf-8").split(",")[0]),
                        "customer": int(line.decode("utf-8").split(",")[1].strip()),
                    }
                )
            line_count += 1

        return validated_data

    @classmethod
    def handle_barcode_file(cls, file):
        line_count = 0
        seen = set()
        validated_data = []
        for line in file:
            if line_count != 0:
                if line in seen or line.decode("utf-8").split(",")[1] == "\n":
                    print(
                        "Repeated values or order's without barcode!",
                        line.decode("utf-8").split(","),
                    )
                else:
                    seen.add(line)
                    validated_data.append(
                        {
                            "barcode": int(line.decode("utf-8").split(",")[0]),
                            "order_id": int(line.decode("utf-8").split(",")[1].strip()),
                        }
                    )

            line_count += 1

        return validated_data

    @classmethod
    def write_answer_to_file(cls, final_answer):
        with open("file_with_answer.csv", "w") as csv_file:
            csv_file = csv.writer(
                csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )

            for answer in final_answer:
                csv_file.writerow(answer)
