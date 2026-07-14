---
type: Concept
title: Prototype vs. Class-Based Objects
description: An object system built on cloning concrete objects, rather than instantiating abstract classes, collapses the class/instance distinction entirely.
book: seven-languages-seven-weeks
chapters: [3]
tags: [object-orientation, prototypes, inheritance, abstraction, language-design]
created: 2026-07-12
---

# Prototype vs. Class-Based Objects

## Definition

In a class-based language, you define an abstract template (a class) and then instantiate concrete objects from it — the class and its instances are different kinds of things. In a prototype-based language like Io, "every object is a clone of an existing object rather than a class": there are no classes at all, only objects, and you make a new one by cloning an existing object and adding or overriding its slots. The distinction between "the mold" and "the thing made from the mold" disappears — an object can serve as another object's prototype without being any special kind of entity.

## In the Book

Tate develops this through Io's `clone` mechanism directly in the interpreter. He starts with `Vehicle := Object clone`, noting that "Vehicle is not a class. It's not a template used to create objects. It is an object, based on the Object prototype." Objects are "little more than a collection of slots" — key/value pairs reached by sending the slot's name as a message — and when a slot isn't found on an object, Io walks up to the object's prototype and tries there, which is how inheritance works without any inheritance keyword. He then builds `Car := Vehicle clone` and `ferrari := Car clone`, showing that `ferrari description` resolves by forwarding the message up through `Car` to `Vehicle`, where the slot actually lives. The one wrinkle is that "types" in Io are just a naming convention, not a language feature: an object whose name starts with an uppercase letter (like `Car` or `Ferrari`) gets a `type` slot set automatically, so programmers can still organize code around "kinds" of things — but this is sugar layered on top of pure object-cloning, not a separate mechanism the way `class` is in Ruby or Java.

## Why It Matters

Prototype-based inheritance shows that "template that stamps out instances" and "example you copy and adapt" are two different ways to solve the same design problem — reuse an existing shape while allowing variation — and neither is a logical necessity of object orientation. This reframes class hierarchies in any OOP language as one implementation choice among several: JavaScript's underlying object model, spreadsheet templates, "copy this doc and edit it," and version-control forking all solve the reuse-with-variation problem the prototype way rather than the class way. Recognizing which strategy a system uses changes how you predict what happens when the "original" changes after copies have already diverged.
