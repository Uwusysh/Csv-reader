
## Script Overview

This script reads a CSV file and converts each column header into a **key** and its corresponding cell value into a **value**. The output is printed to the console and also saved in a text file named `output.txt`.

For example, given a CSV row:

```
Invoice_Number,Date,Recipient_Name  
100,2025-09-25,John Doe  
```

The script outputs:

```
Invoice_Number: 100  
Date: 2025-09-25  
Recipient_Name: John Doe  
```

## How to Run

1. Save your CSV file as `input.csv` in the same folder as the script.
2. Run the script from the terminal:

   ```bash
   python csv_to_key_value.py
   ```
3. The results will be printed in the console and also stored in `output.txt`.

## Notes

* Currently, the script processes only the **first row** of the CSV, as shown in the assignment example.
* It uses only the built-in Python `csv` library, so no external dependencies are required.
