class DynamicArray<T> {
  private length = 0;
  private array: (T | undefined)[] = new Array(2).fill(null);

  constructor() {}

  public get value(): (T | undefined)[] {
    return this.array.slice(0, this.length);
  }

  public get size(): number {
    return this.length;
  }

  public get isEmpty(): boolean {
    return this.size === 0;
  }

  public get(index: number): T | undefined {
    return this.array[index];
  }

  public set(index: number, entry: T) {
    if (index >= this.length) {
      this.length = index + 1;
    }

    this.array[index] = entry;
  }

  public clear() {
    for (let i = 0; i < this.length; i++) {
      this.array[i] = undefined;
    }

    this.length = 0;
  }

  public add(entry: T) {
    const arrayLength = this.array.length;

    if (this.length === arrayLength) {
      this.array = this.array.concat(new Array(arrayLength).fill(null));
    }

    this.array[this.length++] = entry;
  }

  public removeAt(index: number) {
    if (index >= this.size || index < 0) {
      throw new RangeError("No index");
    }

    const data = this.array[index];
    this.array[index] = undefined;
    return data;
  }

  public remove(entry: T) {
    for (let i = 0; i < this.length; i++) {
      if (this.array[i] === entry) {
        return this.removeAt(i);
      }
    }

    return false;
  }
}

const array = new DynamicArray();
array.add(3);
array.add(3);
array.set(4, "jsjsjs");
array.set(3, "jsjsjs");
console.log(array.remove(3));
console.log({ aaaa: array.value, leee: array.size });
