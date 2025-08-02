#!/usr/bin/env python3
"""
Script to verify and manage item ownership in the Flask Market database
"""

import sys
import os
# Add parent directory to path to import from market package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from market import app, db
from market.models import Item, User

def view_all_data():
    """View all users and items with their ownership"""
    with app.app_context():
        print("=== USERS IN DATABASE ===")
        users = User.query.all()
        if users:
            for user in users:
                print(f"ID: {user.id}, Username: {user.username}, Email: {user.email_address}, Budget: ${user.budget}")
        else:
            print("No users found in database!")
            return
        
        print("\n=== ITEMS AND OWNERSHIP ===")
        items = Item.query.all()
        if items:
            for item in items:
                owner_name = "None"
                if item.owner:
                    owner_user = User.query.get(item.owner)
                    if owner_user:
                        owner_name = owner_user.username
                print(f"ID: {item.id}, Name: {item.name}, Price: ${item.price}, Owner: {owner_name}")
        else:
            print("No items found in database!")

def verify_iphone_assignment():
    """Specifically verify if iPhone is assigned to jsc"""
    with app.app_context():
        # Look for iPhone (could be 'iPhone' or 'iPhone 10')
        iphone = Item.query.filter(Item.name.like('%iPhone%')).first()
        jsc_user = User.query.filter_by(username='jsc').first()
        
        if not iphone:
            print("❌ No iPhone found in database!")
            return
        
        if not jsc_user:
            print("❌ User 'jsc' not found in database!")
            return
        
        if iphone.owner == jsc_user.id:
            print(f"✅ SUCCESS: {iphone.name} is owned by {jsc_user.username}")
            print(f"   Item ID: {iphone.id}")
            print(f"   User ID: {jsc_user.id}")
            print(f"   Price: ${iphone.price}")
        else:
            current_owner = "None"
            if iphone.owner:
                owner_user = User.query.get(iphone.owner)
                if owner_user:
                    current_owner = owner_user.username
            print(f"❌ {iphone.name} is currently owned by: {current_owner}")
            print(f"   Expected owner: {jsc_user.username}")

def main():
    """Main function"""
    print("Flask Market - Ownership Verification")
    print("====================================")
    
    while True:
        print("\nChoose an option:")
        print("1. View all data (users and items)")
        print("2. Verify iPhone assignment to jsc")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            view_all_data()
        elif choice == '2':
            verify_iphone_assignment()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()