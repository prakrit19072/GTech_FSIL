from sec_edgar_downloader import Downloader
import os

# Function to download 10-K filings for a given ticker and range of years
def download_10k_filings(ticker, start_year, end_year, company_name, email):
    # Create a directory for the 10-K filings if it doesn't exist
    save_path = os.path.join("..", "10K-Filings")  # Save the filings outside the current folder in a directory named "10K"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Create a directory for the company within the 10-K folder
    company_path = os.path.join(save_path, ticker)
    if not os.path.exists(company_path):
        os.makedirs(company_path)

    
    #ORCL                                             
# Oracle Corporation
# investor_relations@oracle.com
    # Initialize the downloader
    dlr = Downloader(company_name, email, os.getcwd())

    # Iterate through each year in the specified range
    for year in range(start_year, end_year + 1):
        try:
            # Download the 10-K filing for the given ticker and year
            dlr.get("10-K",ticker, before = f"{year}-12-31", after = f"{year}-01-01",download_details=False)

            # Move the downloaded filing to the company's directory within the 10-K folder
            # original_path = os.path.join(dlr.save_dir, f"{ticker}_{year}_10K.xml")
            # new_path = os.path.join(company_path, f"{ticker}_{year}_10K.xml")
            # os.rename(original_path, new_path)

            print(f"Downloaded 10-K filing for {ticker} for the year {year}")
        except Exception as e:
            print(f"Error downloading 10-K filing for {ticker} for the year {year}: {e}")


start_year = 1995  # Start year for downloading filings
end_year = 2023  # End year for downloading filings

ticker = input()
company_name = input()
email = input()
# Call the function to download 10-K filings for the specified ticker and years
download_10k_filings(ticker, start_year, end_year, company_name, email)
