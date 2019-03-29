import sqlite3

conn = sqlite3.connect('datasets/rpg_db.sqlite3')

c = conn.cursor()

print("How many total Characters are there?")
c.execute(
    "SELECT COUNT(*)"
    "FROM   charactercreator_character"
)
print(c.fetchone())


print("How many of each specific subclass?")
c.execute("""\
SELECT (
    SELECT COUNT(*)
    FROM   charactercreator_cleric
    ) AS clerics,
    (
    SELECT COUNT(*)
    FROM   charactercreator_fighter
    ) AS fighters,
    (
    SELECT COUNT(*)
    FROM   charactercreator_mage
    ) AS mages,
	(
    SELECT COUNT(*)
    FROM   charactercreator_necromancer
    ) AS necromancers,
	(
    SELECT COUNT(*)
    FROM   charactercreator_thief
    ) AS thieves
""")
print(c.fetchall())


print("How many total Items?")
c.execute("""\
SELECT COUNT(*)
FROM   armory_item
""")
print(c.fetchone())


print("How many of the Items are weapons? How many are not?")
c.execute("""\
SELECT COUNT(*)
FROM armory_item AS item
LEFT JOIN armory_weapon AS weapon
ON item.item_id = weapon.item_ptr_id
WHERE weapon.item_ptr_id IS NOT NULL""")
print(c.fetchone())

c.execute("""\
SELECT COUNT(*)
FROM armory_item AS item
LEFT JOIN armory_weapon AS weapon
ON item.item_id = weapon.item_ptr_id
WHERE weapon.item_ptr_id IS NULL""")
print(c.fetchone())


print("How many Items does each character have? (Return first 20 rows)")
c.execute("""\
SELECT character_id, COUNT(*) n_items
FROM charactercreator_character_inventory as inventory
GROUP BY inventory.character_id
LIMIT 20
""")
print(c.fetchall())


print("How many Weapons does each character have? (Return first 20 rows)")
c.execute("""\
SELECT COUNT(*)
FROM charactercreator_character_inventory as inventory, armory_weapon as weapon
WHERE inventory.item_id = weapon.item_ptr_id
GROUP BY inventory.character_id
LIMIT 20
""")
print(c.fetchall())

print("On average, how many Items does each Character have?")
c.execute("""\
SELECT AVG(n_items)
FROM (
	SELECT character_id, COUNT(*) AS n_items
	FROM charactercreator_character_inventory as inventory
	GROUP BY inventory.character_id
)
""")
print(c.fetchall())


print("On average, how many Weapons does each character have?")
c.execute("""\
SELECT AVG(n_weapons)
FROM (
    SELECT character_id, COUNT(*) AS n_weapons
    FROM charactercreator_character_inventory as inventory, armory_weapon as weapon
    WHERE inventory.item_id = weapon.item_ptr_id
    GROUP BY inventory.character_id
)
""")
print(c.fetchall())