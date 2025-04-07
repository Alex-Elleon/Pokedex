import { StatusBar } from 'expo-status-bar';
import { Pressable, StyleSheet, Text, TextInput, View, Image} from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View>{/*container-image*/}
        <Image
          source={{ uri: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png" }}
          width={200}
          height={200}
        />
      </View>
      <View>{/*container-form*/}
        <Text style={styles.title}>Iniciar Sesion</Text>{/* title */}
        <Text style={styles.label}>Correo:</Text>{/* label */}
        <TextInput style={styles.input}/>
        <Text style={styles.label}>Contraseña</Text>{/* label */}
        <TextInput style={styles.input}/>
        <Pressable style={styles.send}>
          <Text style={styles.send.textButton}>Enviar</Text>
        </Pressable>
      </View>
      <View> {/* container-footer */}
        <Text  style={styles.containerFooter.texts}>¿Olvidaste tu contraseña?</Text>
        <Text style={styles.containerFooter.texts}>Registrate</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center'
  },
  title:{
    fontSize:30,
    fontWeight:'bold'
  },
  label:{
    fontSize:20,
    fontWeight:'bold'
  },
  input:{
    borderRadius: 10,
    borderWidth: 2,
    borderColor: 'black',
    fontSize: 20,
    height: 50,
    width: "auto",
    backgroundColor: 999999,
  },
  send:{
    backgroundColor: 'red',
    color: 'black',
    fontSize: 20,
    fontWeight: 'bold',
    borderRadius: 10,
    alignItems: 'center',
    width: "auto",
    height: "auto",
  textButton:{
    color: 'black',
    fontSize: 20,
    fontWeight: 'bold',
  }
  },
  containerFooter:{
    justifyContent: 'space-between',
    texts:{
      fontSize: 20,
      margin: 5
    }
  }
});
