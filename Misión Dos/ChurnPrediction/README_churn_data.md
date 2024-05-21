
# Descripción del archivo churn_data.xlsx

El archivo `churn_data.xlsx` contiene datos ficticios de clientes utilizados para predecir si un cliente va a abandonar el servicio en un futuro cercano. A continuación, se describen las etiquetas y los valores posibles para cada columna en el archivo.

## Columnas del DataFrame

1. **CustomerID**:
   - **Descripción**: Identificador único para cada cliente.
   - **Tipo de Datos**: Entero.

2. **Gender**:
   - **Descripción**: Género del cliente.
   - **Valores Posibles**: `Male`, `Female`.

3. **SeniorCitizen**:
   - **Descripción**: Indica si el cliente es una persona mayor.
   - **Valores Posibles**: `0` (No es persona mayor), `1` (Es persona mayor).

4. **Partner**:
   - **Descripción**: Indica si el cliente tiene pareja.
   - **Valores Posibles**: `Yes`, `No`.

5. **Dependents**:
   - **Descripción**: Indica si el cliente tiene dependientes.
   - **Valores Posibles**: `Yes`, `No`.

6. **Tenure**:
   - **Descripción**: Número de meses que el cliente ha estado con la empresa.
   - **Tipo de Datos**: Entero.

7. **PhoneService**:
   - **Descripción**: Indica si el cliente tiene servicio telefónico.
   - **Valores Posibles**: `Yes`, `No`.

8. **MultipleLines**:
   - **Descripción**: Indica si el cliente tiene múltiples líneas telefónicas.
   - **Valores Posibles**: `Yes`, `No`.

9. **InternetService**:
   - **Descripción**: Tipo de servicio de internet que tiene el cliente.
   - **Valores Posibles**: `DSL`, `Fiber optic`, `No` (No tiene servicio de internet).

10. **OnlineSecurity**:
    - **Descripción**: Indica si el cliente tiene servicio de seguridad en línea.
    - **Valores Posibles**: `Yes`, `No`.

11. **OnlineBackup**:
    - **Descripción**: Indica si el cliente tiene servicio de respaldo en línea.
    - **Valores Posibles**: `Yes`, `No`.

12. **DeviceProtection**:
    - **Descripción**: Indica si el cliente tiene servicio de protección de dispositivos.
    - **Valores Posibles**: `Yes`, `No`.

13. **TechSupport**:
    - **Descripción**: Indica si el cliente tiene servicio de soporte técnico.
    - **Valores Posibles**: `Yes`, `No`.

14. **StreamingTV**:
    - **Descripción**: Indica si el cliente tiene servicio de streaming de TV.
    - **Valores Posibles**: `Yes`, `No`.

15. **StreamingMovies**:
    - **Descripción**: Indica si el cliente tiene servicio de streaming de películas.
    - **Valores Posibles**: `Yes`, `No`.

16. **Contract**:
    - **Descripción**: Tipo de contrato que tiene el cliente.
    - **Valores Posibles**: `Month-to-month` (Mensual), `One year` (Anual), `Two year` (Bianual).

17. **PaperlessBilling**:
    - **Descripción**: Indica si el cliente tiene facturación electrónica.
    - **Valores Posibles**: `Yes`, `No`.

18. **PaymentMethod**:
    - **Descripción**: Método de pago del cliente.
    - **Valores Posibles**: `Electronic check` (Cheque electrónico), `Mailed check` (Cheque por correo), `Bank transfer (automatic)` (Transferencia bancaria automática), `Credit card (automatic)` (Tarjeta de crédito automática).

19. **MonthlyCharges**:
    - **Descripción**: Cargos mensuales que paga el cliente.
    - **Tipo de Datos**: Flotante.

20. **TotalCharges**:
    - **Descripción**: Cargos totales que ha pagado el cliente.
    - **Tipo de Datos**: Flotante.

21. **Churn**:
    - **Descripción**: Indica si el cliente ha abandonado el servicio.
    - **Valores Posibles**: `Yes` (Ha abandonado), `No` (No ha abandonado).

## Ejemplo de Datos en el DataFrame

Aquí hay un ejemplo de cómo se ven los datos en el DataFrame:

| CustomerID | Gender | SeniorCitizen | Partner | Dependents | Tenure | PhoneService | MultipleLines | InternetService | OnlineSecurity | OnlineBackup | DeviceProtection | TechSupport | StreamingTV | StreamingMovies | Contract | PaperlessBilling | PaymentMethod               | MonthlyCharges | TotalCharges | Churn |
|------------|--------|---------------|---------|------------|--------|--------------|---------------|-----------------|----------------|--------------|------------------|-------------|-------------|-----------------|----------|------------------|-----------------------------|----------------|--------------|-------|
| 1          | Male   | 0             | Yes     | No         | 5      | Yes          | No            | DSL             | No             | Yes          | No               | No          | No          | Yes             | Month-to-month | Yes              | Electronic check            | 29.85          | 188.95       | No    |
| 2          | Female | 0             | No      | No         | 2      | Yes          | No            | DSL             | Yes            | No           | No               | Yes         | No          | No              | Two year     | No               | Mailed check                | 56.95          | 108.15       | No    |
| 3          | Female | 1             | No      | No         | 8      | No           | No            | Fiber optic     | No             | Yes          | Yes              | No          | Yes         | Yes             | One year      | Yes              | Bank transfer (automatic)   | 53.85          | 869.45       | Yes   |

### Descripción de las Columnas

- **CustomerID**: Identificador único de cada cliente.
- **Gender**: Género del cliente.
- **SeniorCitizen**: Indicador de si el cliente es una persona mayor.
- **Partner**: Indicador de si el cliente tiene pareja.
- **Dependents**: Indicador de si el cliente tiene dependientes.
- **Tenure**: Número de meses que el cliente ha estado con la empresa.
- **PhoneService**: Indicador de si el cliente tiene servicio telefónico.
- **MultipleLines**: Indicador de si el cliente tiene múltiples líneas telefónicas.
- **InternetService**: Tipo de servicio de internet del cliente.
- **OnlineSecurity**: Indicador de si el cliente tiene servicio de seguridad en línea.
- **OnlineBackup**: Indicador de si el cliente tiene servicio de respaldo en línea.
- **DeviceProtection**: Indicador de si el cliente tiene servicio de protección de dispositivos.
- **TechSupport**: Indicador de si el cliente tiene servicio de soporte técnico.
- **StreamingTV**: Indicador de si el cliente tiene servicio de streaming de TV.
- **StreamingMovies**: Indicador de si el cliente tiene servicio de streaming de películas.
- **Contract**: Tipo de contrato del cliente.
- **PaperlessBilling**: Indicador de si el cliente tiene facturación electrónica.
- **PaymentMethod**: Método de pago del cliente.
- **MonthlyCharges**: Cargos mensuales del cliente.
- **TotalCharges**: Cargos totales del cliente.
- **Churn**: Indicador de si el cliente ha abandonado el servicio.

Este DataFrame proporciona una visión general de los atributos y características que se utilizan para predecir si un cliente va a abandonar el servicio. Cada fila representa a un cliente diferente y sus respectivos detalles.
