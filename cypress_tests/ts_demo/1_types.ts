const isStart: boolean = true
const isEnd: boolean = false

const isNumber: number = 1423
const isFloat: number = 1.423

const isString: string = 'typescript'

const numberArray: number[] = [1, 1, 2, 3, 8, 13]
const numberArray2: Array<number> = [1, 1, 2, 3, 8, 13]
const words: string[] = ['Hello', 'typescript']
const contact: [string, number] = ['Vladlen', +37112345678]

let variable: any = 1234
variable = 'Bla-bla'

function sayMyName(name: string): void {
    console.log(name)
}
sayMyName('bla bla name')

function error(message: string): never {
    throw new Error(message);
  }

type Login = string 
const login: login = 'admin'
type ID = string | number
const id1: ID = '1'
const id2: ID =  1
type SomeValue = string | null | undefined


