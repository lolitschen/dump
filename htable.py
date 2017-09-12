"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for x in xrange(5)]


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """

    if type(o) is int:
        return o
    else if type(o) is str:
        h = 0
        for c in o:
            h += h*31 + ord(c)
    else
        return None


def bucket_indexof(bucket, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    for idx, val in enumerate(bucket):
        if val == key:
            return idx
    return None


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """

    bucket = table[hashcode(key) % len(table)]

    b_index = bucket_indexof(bucket, key)
    if b_index is None:
        bucket.append((key, value))
    else:
        bucket[b_index] = (key, value)

def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """

    bucket = table[hashcode(key) % len(table)]
    b_index = bucket_indexof(bucket, key)

    result = None
    if b_index is not None:
        result = (bucket[b_index])[1]
    return result



def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    output = ""
    for index, bucket in enumerate(table):
        output += str(index).zfill(4) + "->"
        for entry in bucket:
            data = list(entry)
            output += data[0] + ":" + data[1] + ","
        #clear extra ,
        if output[-1] == ',':
            output = output[:-1]
        output += "\n"
    return output

def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """

    output = "{"
    for bucket in table:
        for entry in bucket:
            data = list(entry)
            output += data[0] + ":" + data[1] + ","
    #clear extra ,
    if output[-1] == ',':
        output = output[:-1]
    output += "}"
    return output
