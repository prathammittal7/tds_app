import streamlit as st

def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

def main():
    st.title("Find the Largest Among Three Numbers")
    
    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write("The largest number is:", largest)

if __name__ == "__main__":
    main()
