def main():
  # Print a line with 32 dashes
  print("-" * 32)

  # Ask for user input and print "f(x) :"
  x = input("f(x) :")

  # Validate the user input
  if ")" not in x:
    # If the input doesn't end in ")", print an error message and exit the script
    print("Input error. Exiting...")
    return
  else:
    # Check if the input ends with one of the specified endings using a loop
    endings = ["=0", ">0", ">=0", "<0", "<=0"]
    ends_with_ending = False
    for ending in endings:
      if x.endswith(ending):
        ends_with_ending = True
        break

    # If the input doesn't end with one of the specified endings, add "=0" to the end
    if not ends_with_ending:
      x += "=0"

  # After input validation, call the proccess_input function with the user input as an argument
  proccess_input(x)

def proccess_input(x):
  # Extract the terms from the input string
  terms = extract_terms(x)
  
  # Create a table of signs for the terms
  table = create_table(terms)
  
  # Print the table of signs
  print_table(table)
  
  # Output the interval that x belongs to
  output_interval(table)

def print_table(table):
  """Prints the table of signs for the given terms."""
  # Print a header row for the table
  print("{:>5s} | {:>5s} | {:>5s}".format("Sign", "Degree", "Value"))
  print("-" * 18)
  
  # Iterate over the rows of the table
  for row in table:
    # Extract the sign, degree, and value from the row
    sign = row["sign"]
    degree = row["degree"]
    value = row["value"]
    
    # Print the row
    if value is None:
      print("{:>5d} | {:>5d} | {:>5s}".format(sign, degree, "-"))
    else:
      print("{:>5d} | {:>5d} | {:>5.2f}".format(sign, degree, value))

def extract_terms(x):
  """Extracts the individual terms of an equation or inequality."""
  # Remove any ending characters (e.g. "=0", ">0", etc.) from the input string
  x = x.rstrip("=0")
  x = x.rstrip(">0")
  x = x.rstrip(">=0")
  x = x.rstrip("<0")
  x = x.rstrip("<=0")
  
  # Split the input string on the plus and minus signs
  terms = []
  term = ""
  for c in x:
    if c in ["+", "-"]:
      terms.append(term)
      term = c
    else:
      term += c
  terms.append(term)
  
  # Filter out empty terms
  terms = [term for term in terms if term]
  
  return terms

def create_table(terms):
  """Creates a table of signs for the given terms."""
  # Initialize the table to an empty list
  table = []
  
  # Iterate over the terms
  for term in terms:
    # Check if the term is a constant term
    if "/" in term or term.isdigit():
      # The term is a constant term
      sign, value = extract_constant(term)
      degree = 0
    else:
      # The term is a variable term
      sign, degree = extract_variable(term)
      value = None
      
    # Add a row to the table for the term
    row = {"sign": sign, "degree": degree, "value": value}
    table.append(row)
  
  return table

def output_interval(table, sign):
  """Outputs the interval that x belongs to based on the given table of signs and the sign of the equation or inequality."""
  # Initialize the interval to an empty string
  interval = ""
  
  # Iterate over the rows of the table
  for row in table:
    # Extract the degree and value from the row
    degree = row["degree"]
    value = row["value"]
    
    # Check the degree of the term
    if degree == 0:
      # The term is a constant term
      if sign == "=":
        # The equation or inequality is an equality
        if value > 0:
          # The term is positive, so x must be in the positive interval
          interval += "+"
        else:
          # The term is negative, so x must be in the negative interval
          interval += "-"
      elif sign == ">":
        # The equation or inequality is a strict inequality
        if value > 0:
          # The term is positive, so x must be in the positive interval
          interval += "+"
        else:
          # The term is negative, so x must be in the negative interval
          interval += "-"
      elif sign == ">=":
        # The equation or inequality is a non-strict inequality
        if value >= 0:
          # The term is non-negative, so x must be in the positive interval
          interval += "+"
        else:
          # The term is negative, so x must be in the negative interval
          interval += "-"
      elif sign == "<":
        # The equation or inequality is a strict inequality
        if value < 0:
          # The term is negative, so x must be in the positive interval
          interval += "+"
        else:
          # The term is positive, so x must be in the negative interval
          interval += "-"
      elif sign == "<=":
        # The equation or inequality is a non-strict inequality
        if value <= 0:
          # The term is non-positive, so x must be in the positive interval
          interval += "+"
        else:
          # The term is positive, so x must be in the negative interval
          interval += "-"
    else:
      # The term is a variable term
      if degree == 1:
        # The term is linear, so x can be in either interval
        interval += "±"
      else:
        # The term is quadratic, so x must be in the positive interval
        interval += "+"
  
  # Output the interval
  if interval:
    # The interval is not empty, so output the interval
    print("x E {}".format(interval))
  else:
    # The interval is empty, so output a default interval
    print("x E R")

def extract_variable(term):
  """Extracts the sign and degree of a variable term."""
  # Initialize the sign and degree to default values
  sign = 1
  degree = 1
  
  # Check if the term starts with a plus or minus sign
  if term[0] in ["+", "-"]:
    # The term starts with a sign
    if term[0] == "+":
      sign = 1
    else:
      sign = -1
      
    # Remove the sign from the term
    term = term[1:]
  
  # Check if the term contains an exponentiation symbol
  if "^" in term:
    # The term contains an exponentiation symbol
    base, exponent = term.split("^")
    degree = int(exponent)
  else:
    # The term doesn't contain an exponentiation symbol
    degree = 1
  
  return sign, degree

def extract_constant(term):
  """Extracts the sign and value of a constant or variable term."""
  # Initialize the sign and value to default values
  sign = 1
  value = None
  
  # Check if the term starts with a plus or minus sign
  if term[0] in ["+", "-"]:
    # The term starts with a sign
    if term[0] == "+":
      sign = 1
    else:
      sign = -1
      
    # Remove the sign from the term
    term = term[1:]
  
  # Check if the term is a constant term
  if "/" in term or term.isdigit():
    # The term is a constant term
    if "/" in term:
      # The term contains a division symbol
      numerator, denominator = term.split("/")
      value = float(numerator) / float(denominator)
    else:
      # The term doesn't contain a division symbol
      value = float(term)
  else:
    # The term is a variable term
    value = None
  
  return sign, value

if __name__ == "__main__":
  main()
