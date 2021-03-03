FROM python:3
ADD show_data.py /
ADD mFile.txt /
CMD [ "python", "./show_data.py"]
