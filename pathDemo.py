from pathlib import Path

# Absolute path
# Relative path

path = Path("ecommerce")
print(path.exists())

emails_path = Path("emails")
print(emails_path.exists())
if emails_path.exists() == False:
    emails_path.mkdir()

emails_path.rmdir()


pa = Path()
print(pa.glob('*.py'))
# iterating glob object
for file in pa.glob('*.py'):
    print(file)