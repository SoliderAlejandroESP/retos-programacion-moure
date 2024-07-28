// Operaciones con cadenas de caracteres
const cadena = "Hola a todos!"

console.log(cadena.replace("o", "p"))
console.log(cadena.split(" "))
console.log(cadena.length)
console.log(cadena.charCodeAt(0))
console.log(cadena.substring(7))
console.log(cadena.substring(0, 4))
console.log(cadena.charAt(4))
console.log(cadena[4])
console.log(cadena.concat(" Subnormales"))
console.log(cadena.endsWith("todos!"))
console.log(cadena.startsWith("Hola"))
console.log(cadena.includes("Hola"))
console.log(cadena.indexOf("o"))
console.log(cadena.lastIndexOf("o"))
console.log(cadena.toLowerCase())
console.log(cadena.toUpperCase())
console.log(cadena.split(" ").join(""))

console.log(cadena)

// Dificultad addicional
const palabra1 = "aarr"
const palabra2 = "araa"

function isPalindrome(string1, string2) {
  if (string1.length !== string2.length) {
    return false
  }

  const lowerString1 = string1.toLowerCase()
  const lowerString2 = string2.toLowerCase()

  return lowerString2.split("").reverse().join("") === lowerString1
}

function isAnagram(string1, string2) {
  if (string1.length !== string2.length) {
    return false
  }

  const arrayString1 = string1.toLowerCase().split("").sort()
  const arrayString2 = string2.toLowerCase().split("").sort()

  for (let wordIndex = 0; wordIndex < arrayString1.length; wordIndex++) {
    if (arrayString1[wordIndex] !== arrayString2[wordIndex]) {
      return false
    }
  }

  return true
}

console.log(isAnagram(palabra1, palabra2))