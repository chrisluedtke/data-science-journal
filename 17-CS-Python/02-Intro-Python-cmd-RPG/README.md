# Intro to Python II

Up to this point, you've gotten your feet wet by working on a bunch of small Python programs. In this module, we're going to continue to solidify your Python chops by implementing a full-featured project according to a provided specification.


## What We're Building
[What's an Adventure Game? ![vid](https://tk-assets.lambdaschool.com/7928cdb4-b8a3-45a6-b231-5b9d1fc1e002_ScreenShot2019-03-22at5.47.28PM.png)](https://youtu.be/WaZccFqJUT8)


## Goals

* Put your Python basics into practice by implementing a text adventure game

* Practice writing code that conforms to a specification


## MVP

### Day 1 MVP

* Create the REPL command parser in `adv.py` which allows the player to move to rooms
  in the four cardinal directions.
* Fill out Player and Room classes in `player.py` and `room.py`

### Day 2 MVP

* Make rooms able to hold multiple items
* Make the player able to carry multiple items
* Add items to the game that the user can carry around
* Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser

## Specification

The `/src` directory contains the files `adv.py`, which is where the main logic for the game should live, `room.py`, which will contain the definition of the Room class, and `player.py`, which will contain the definition of the Player class.


* Add a REPL parser to `adv.py` that accepts directional commands to move the player
  * After each move, the REPL should print the name and description of the player's current room
  * Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West
  * The parser should print an error if the player tries to move where there is no room.

* Put the Room class in `room.py` based on what you see in `adv.py`.

  * The room should have `name` and `description` attributes.

  * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    which point to the room in that respective direction.

* Put the Player class in `player.py`.
  * Players should have a `name` and `current_room` attributes


* Create a file called `item.py` and add an `Item` class in there.

  * The item should have `name` and `description` attributes.

     * Hint: the name should be one word for ease in parsing later.

  * This will be the _base class_ for specialized item types to be declared
    later.

* Add the ability to add items to rooms.

  * The `Room` class should be extended with a `list` that holds the `Item`s
    that are currently in that room.

  * Add functionality to the main loop that prints out all the items that are
    visible to the player when they are in that room.

* Add capability to add `Item`s to the player's inventory. The inventory can
  also be a `list` of items "in" the player, similar to how `Item`s can be in a
  `Room`.

* Add a new type of sentence the parser can understand: two words.

  * Until now, the parser could just understand one sentence form:

     `verb`

    such as "n" or "q".

  * But now we want to add the form:

    `verb` `object`

    such as "take coins" or "drop sword".

  * Split the entered command and see if it has 1 or 2 words in it to determine
    if it's the first or second form.

* Implement support for the verb `get` followed by an `Item` name. This will be
  used to pick up `Item`s.

  * If the user enters `get` or `take` followed by an `Item` name, look at the
    contents of the current `Room` to see if the item is there.

     * If it is there, remove it from the `Room` contents, and add it to the
       `Player` contents.

     * If it's not there, print an error message telling the user so.

     * Add an `on_take` method to `Item`.

        * Call this method when the `Item` is picked up by the player.

        * `on_take` should print out "You have picked up [NAME]" when you pick up an item.

        * The `Item` can use this to run additional code when it is picked up.

     * Add an `on_drop` method to `Item`. Implement it similar to `on_take`.

* Implement support for the verb `drop` followed by an `Item` name. This is the
  opposite of `get`/`take`.

* Add the `i` and `inventory` commands that both show a list of items currently
  carried by the player.


## Stretch Goals

In arbitrary order:

* Add more rooms

* Add scoring

* Subclass items into treasures

* Add a subclass to `Item` called `LightSource`.

  * During world creation, add a `lamp` `LightSource` to a convenient `Room`.

  * Override `on_drop` in `LightSource` that tells the player "It's not wise to
  drop your source of light!" if the player drops it. (But still lets them drop
  it.)

  * Add an attribute to `Room` called `is_light` that is `True` if the `Room` is
  naturally illuminated, or `False` if a `LightSource` is required to see what
  is in the room.

  * Modify the main loop to test if there is light in the `Room` (i.e. if
    `is_light` is `True` **or** there is a `LightSource` item in the `Room`'s
    contents **or** if there is a `LightSource` item in the `Player`'s contents).

  * If there is light in the room, display name, description, and contents as
    normal.

  * If there isn't, print out "It's pitch black!" instead.

  * Hint: `isinstance` might help you figure out if there's a `LightSource`
    among all the nearby `Item`s.

  * Modify the `get`/`take` code to print "Good luck finding that in the dark!" if
  the user tries to pick up an `Item` in the dark.

* Add methods to notify items when they are picked up or dropped

* Add light and darkness to the game

* Add more items to the game.

* Add a way to win.

* Add more to the parser.

  * Remember the last `Item` mentioned and substitute that if the user types
    "it" later, e.g.

    ```
    take sword
    drop it
    ```

  * Add `Item`s with adjectives, like "rusty sword" and "silver sword".

    * Modify the parser to handle commands like "take rusty sword" as well as
      "take sword".

      * If the user is in a room that contains both the rusty sword _and_ silver
        sword, and they type "take sword", the parser should say, "I don't know
        which you mean: rusty sword or silver sword."

* Modify the code that calls `on_take` to check the return value. If `on_take`
  returns `False`, then don't continue picking up the object. (I.e. prevent the
  user from picking it up.)

  * This enables you to add logic to `on_take` to code things like "don't allow
    the user to pick up the dirt unless they're holding the shovel.

* Add monsters.

* Add the `attack` verb that allows you to specify a monster to attack.

* Add an `on_attack` method to the monster class.

* Similar to the `on_take` return value modification, above, have `on_attack`
  prevent the attack from succeeding unless the user possesses a `sword` item.

* Come up with more stretch goals! The sky's the limit!
