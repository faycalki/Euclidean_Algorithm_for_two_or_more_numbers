def reveal_license_options():
    license_input = input("This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\nThis is free software, and you are welcome to redistribute it under certain conditions; type `show d' for the disclaimer.\nYou may hit enter to continue: ")
    license_details(license_input)
    
def license_details(input):
    if input == "show w":
        print("This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program.  If not, see <https://github.com/faycalki>.")
    elif input == "show d":
        print("This project is intended to be used for legal purposes only, and is pursuant to the license terms and conditions provided. For ther remaining warranties refer to the license file packaged with this, if you can not find it then obtain one for the corresponding project from <https://github.com/faycalki>. ")
    else: 
        pass