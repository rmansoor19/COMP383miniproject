# COMP383miniproject


Prior to completing this project, you need to have Python 3 and BioPython installed

INSTALLING SRAtoolkit

1. Install SRAtoolkit onto your downloads folder using this link:
http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-mac64.tar.gz
2. (Unzip the Archive) using this command:
tar -vxzf  /Users/your_user_name/Downloads/sratoolkit.current-mac64.tar.gz
3. Add the unzipped file to your environment path:
export PATH=$PATH:/Users/your_user_name/Downloads/sratoolkit.2.6.3-mac64/bin/
4. Check if you have it correct installed using the command “which fastq-dump” which will result in “/Users/your_user_name/Downloads/sratoolkit.2.6.3-mac64/bin//fastq-dump”

INSTALLING SPAdes: 

1. Install SPAdes using this link: https://cab.spbu.ru/software/spades/ and click the link: Download SPAdes binaries for MacOS
2. Click on the downloaded file to unzip the archive, which will release a file called “SPAdes-3.15.4-Darwin”.

NOTE: When running this code, errors may arise when utilizing the tools. The error may say “move to trash” or “cancel”. This will stop running the program. Please go into settings on your Mac—> Security and Privacy—> and then press “Allow Anyway”. You may need to do this a couple times to allow the different programs to run. DO NOT press “move to trash”. 

Solutions to issues that may arise when running this code are explained as comments under the commands
