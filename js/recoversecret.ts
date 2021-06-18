// https://www.codewars.com/kata/53f40dff5f9d31b813000774/

function recoverSecret(triplets: string[][]): any {
  let alphabet:string[] = []
  for (let i = 0; i < triplets.length; i++){
    for (let j = 0; j < triplets[i].length; j++){
      if (!alphabet.includes(triplets[i][j])){
        alphabet.push(triplets[i][j]);
      }
    }
  }
  let res:string = ''
  for (let j = 0; j < alphabet.length ; j++){
  for (let i = 0; i < alphabet.length ; i++){
    if (res.includes(alphabet[i])){
      continue;
    }
    let tmp = nextLetter(triplets, alphabet[i], res);
    if (tmp){
      res += tmp
      break
    }
  }}
  return res
}
function nextLetter(triplets: string[][], lett:string, exclude:string):string {
  let before:string = '';
  for (let i = 0; i < triplets.length; i++){
    if (triplets[i][0] == lett){
    }
    if (triplets[i][1] == lett){
      if (!exclude.includes(triplets[i][0]))
      {
        before += triplets[i][0]
      }
    }
    if (triplets[i][2] == lett){
      if (!exclude.includes(triplets[i][0])){
        before += triplets[i][0]
      }
      if (!exclude.includes(triplets[i][1])){
        before += triplets[i][0]
      }
    }
  }
  if (!before) {
    return lett
  }
  return ''
}