# Map

## `interface Map`

- object that let keys be mapped to values
- to replace `Dictionary`

## `abstract Dictionary`

- `abstract` put/get/remove/keys/elements/isEmpty/size
- should not be used, use `Map` instead

## `Hashtable extends Dicationary implements Map`

- `synchronized` put/get/remove/keys/elements/isEmpty/size
- key must be non `null`
- should not be used
    - no thread safe, use `HashMap`
    - thread safe, use `ConcurrentHashMap`

## `HashMap`

- The `HashMap` class is roughly equivalent to `Hashtable`, except that it is unsynchronized and permits nulls.

## `ConcurrentHashMap`

A hash table supporting full concurrency of retrievals and high expected concurrency for updates

#### To avoid **check-then-act** issue

Use `putIfAbsent` or `computeIfAbsent` to replace `if (!map.containsKey(key)) {map.put(key, value)}`

#### Implementation

`volatile Node<K,V>[] table`

#### `put`

if bucket is empty (`null`) -> use CAS to insert 

```java
if (casTabAt(tab, i, null, new Node<K,V>(hash, key, value)))
    break;  // no lock when adding to empty bin
```

```java
static final <K,V> boolean casTabAt(Node<K,V>[] tab, int i, Node<K,V> c, Node<K,V> v) {
        return U.compareAndSetReference(tab, ((long)i << ASHIFT) + ABASE, c, v);
}
```

if bucket is not null:
- synchronized on head of linked list
- synchronized tree root
then use CAS to update value


