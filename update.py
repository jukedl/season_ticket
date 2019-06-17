import openpyxl
import pathlib
import datetime
import monthdelta

folder = pathlib.Path('Y:Documents/Admin/Season Ticket Seat Reservation/')

template = 'seat-reservation.xlsx'

file_to_open = folder / template

wb = openpyxl.load_workbook(file_to_open)

sheet = wb['Form']

new_number = input('Please enter the new season ticket number!: ')
new_validity = input('New start date? dd/mm/yyyy: ')
new_validity_date = datetime.datetime.strptime(new_validity, '%d/%m/%Y')
new_expiry_date = new_validity_date + monthdelta.monthdelta(1)

today = datetime.date.today()

sheet['B5'] = datetime.date.strftime(today, '%d/%m/%Y')
sheet['B8'] = datetime.date.strftime(new_validity_date, '%d/%m/%Y')
sheet['D7'] = new_number
sheet['D8'] = datetime.date.strftime(new_expiry_date, '%d/%m/%Y')

filename = str(today) + template

file_to_save_to = folder / filename

wb.save(filename = file_to_save_to)