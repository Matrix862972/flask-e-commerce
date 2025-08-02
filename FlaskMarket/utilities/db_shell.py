#!/usr/bin/env python3
"""
Database shell script for Flask Market application
Run this script to get an interactive shell with database access
"""

import sys
import os
# Add parent directory to path to import from market package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from market import app, db
from market.models import Item

def create_tables():
    """Create all database tables"""
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

def add_sample_items():
    """Add some sample items to the database"""
    with app.app_context():
        # Check if items already exist
        existing_items = Item.query.all()
        if existing_items:
            print(f"Database already has {len(existing_items)} items:")
            for item in existing_items:
                print(f"  - {item.name} (${item.price})")
            
            choice = input("\nDo you want to add more items anyway? (y/n): ").strip().lower()
            if choice != 'y':
                print("Cancelled adding items.")
                return
        
        # Define sample items to add
        sample_items_data = [
            {'name': 'Laptop', 'price': 900, 'barcode': '123985473165', 'description': 'A high-performance laptop'},
            {'name': 'Keyboard', 'price': 150, 'barcode': '231985128446', 'description': 'Mechanical gaming keyboard'},
            {'name': 'Mouse', 'price': 50, 'barcode': '456789123456', 'description': 'Wireless gaming mouse'},
            {'name': 'Monitor', 'price': 300, 'barcode': '789456123789', 'description': '24-inch 4K monitor'}
        ]
        
        items_added = 0
        for item_data in sample_items_data:
            # Check if item already exists by name or barcode
            existing = Item.query.filter(
                (Item.name == item_data['name']) | 
                (Item.barcode == item_data['barcode'])
            ).first()
            
            if not existing:
                item = Item(**item_data)
                db.session.add(item)
                items_added += 1
                print(f"Added: {item_data['name']}")
            else:
                print(f"Skipped: {item_data['name']} (already exists)")
        
        if items_added > 0:
            db.session.commit()
            print(f"\n{items_added} new items added successfully!")
        else:
            print("\nNo new items were added.")

def show_all_items():
    """Display all items in the database"""
    with app.app_context():
        items = Item.query.all()
        if not items:
            print("No items found in database")
            return
        
        print(f"\nFound {len(items)} items:")
        print("-" * 50)
        for item in items:
            print(f"ID: {item.id}")
            print(f"Name: {item.name}")
            print(f"Price: ${item.price}")
            print(f"Barcode: {item.barcode}")
            print(f"Description: {item.description}")
            print("-" * 50)

def add_custom_item():
    """Add a custom item to the database"""
    with app.app_context():
        print("\nAdd a new item:")
        try:
            name = input("Enter item name: ").strip()
            price = float(input("Enter price: $"))
            barcode = input("Enter barcode: ").strip()
            description = input("Enter description: ").strip()
            
            # Check if item already exists
            existing = Item.query.filter(
                (Item.name == name) | (Item.barcode == barcode)
            ).first()
            
            if existing:
                print(f"Error: Item with name '{name}' or barcode '{barcode}' already exists!")
                return
            
            # Create and add the item
            item = Item(name=name, price=price, barcode=barcode, description=description)
            db.session.add(item)
            db.session.commit()
            
            print(f"Successfully added: {name} (${price})")
            
        except ValueError:
            print("Error: Invalid price entered. Please enter a number.")
        except Exception as e:
            print(f"Error adding item: {e}")

def delete_item():
    """Delete an item from the database"""
    with app.app_context():
        items = Item.query.all()
        if not items:
            print("No items found in database")
            return
        
        print("\nCurrent items:")
        for item in items:
            print(f"ID: {item.id} - {item.name} (${item.price})")
        
        try:
            item_id = int(input("\nEnter the ID of the item to delete: "))
            item = Item.query.get(item_id)
            
            if item:
                name = item.name
                db.session.delete(item)
                db.session.commit()
                print(f"Successfully deleted: {name}")
            else:
                print("Item not found!")
                
        except ValueError:
            print("Error: Please enter a valid ID number.")
        except Exception as e:
            print(f"Error deleting item: {e}")

if __name__ == "__main__":
    print("Flask Market Database Shell")
    print("=" * 30)
    
    while True:
        print("\nOptions:")
        print("1. Create database tables")
        print("2. Add sample items")
        print("3. Show all items")
        print("4. Add custom item")
        print("5. Delete item")
        print("6. Interactive Python shell")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            create_tables()
        elif choice == "2":
            add_sample_items()
        elif choice == "3":
            show_all_items()
        elif choice == "4":
            add_custom_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            print("\nStarting interactive shell...")
            print("Available objects: app, db, Item")
            print("Remember to use 'with app.app_context():' for database operations")
            
            # Start interactive shell with app context
            with app.app_context():
                import code
                code.interact(local=locals())
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
